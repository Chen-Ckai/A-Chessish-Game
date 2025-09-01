import os
import random
import threading
import time

# --- Game settings ---
GRID_SIZE = 6
DIRECTIONS = {
    "north": (-1, 0),
    "south": (1, 0),
    "east": (0, 1),
    "west": (0, -1)
}

# --- Global state ---
player_pos = [0, 0]
pressed_buttons = set()
buttons_to_press = set()
move_limit = 30
moves_used = 0
mode = None
timer_event = threading.Event()
time_left = None  # shared timer state


# --- Helpers ---
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_cell(row, col):
    return board[row][col]


def generate_board():
    board = []
    for r in range(GRID_SIZE):
        row = []
        for c in range(GRID_SIZE):
            cell_type = "blank"
            name = f"cell-{r+1}-{c+1}"
            row.append({"name": name, "type": cell_type})
        board.append(row)
    return board


def place_special_cells(board):
    # Place exit
    while True:
        r, c = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        if (r, c) != (0, 0):
            board[r][c]["type"] = "exit"
            break
    # Place buttons
    for _ in range(5):
        while True:
            r, c = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
            if board[r][c]["type"] == "blank":
                board[r][c]["type"] = "button"
                buttons_to_press.add((r, c))
                break
    return board


def print_mini_map(path=None):
    for r in range(GRID_SIZE):
        row = ""
        for c in range(GRID_SIZE):
            if [r, c] == player_pos:
                row += "😀 "
            elif path and (r, c) in path:
                row += "· "
            elif board[r][c]["type"] == "exit":
                row += "🚪 "
            elif board[r][c]["type"] == "button":
                row += "🔘 " if (r, c) not in pressed_buttons else "✅ "
            else:
                row += "⬜ "
        print(row)


def render_game_state(path=None):
    clear_screen()
    
    print(f"Buttons pressed: {len(pressed_buttons)}/{len(buttons_to_press)} | Moves left: {move_limit - moves_used}")
    print(f"📍 You are at {get_cell(*player_pos)['name']} ({get_cell(*player_pos)['type']})")
    print_mini_map(path)



def start_timer(duration):
    def run():
        global time_left
        time_left = duration
        while time_left > 0 and not timer_event.is_set():
            time.sleep(1)
            time_left -= 1
        if timer_event.is_set():
            return
        print("\n⏰ Time's up! Game over.")
        os._exit(0)
    t = threading.Thread(target=run, daemon=True)
    t.start()



def preview_path(direction, steps):
    dr, dc = DIRECTIONS[direction]
    path = []
    r, c = player_pos
    for _ in range(steps):
        r, c = r + dr, c + dc
        if not (0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE):
            return None
        path.append((r, c))
    return path


def move_player(path):
    global moves_used
    for (r, c) in path:
        player_pos[0], player_pos[1] = r, c
        moves_used += 1
        if board[r][c]["type"] == "button" and (r, c) not in pressed_buttons:
            pressed_buttons.add((r, c))
            print(f"🔘 You pressed a button at {board[r][c]['name']}!")
        if board[r][c]["type"] == "exit":
            if pressed_buttons == buttons_to_press:
                print("🎉 You pressed all buttons and reached the exit! You win!")
                timer_event.set()
                os._exit(0)
            else:
                print("🚪 You found the exit, but not all buttons are pressed!")


# --- Main game ---
board = generate_board()
board = place_special_cells(board)

print("Choose mode: 'timed' or 'move-limited'")
mode = input("> ").strip().lower()
if mode == "timed":
    start_timer(120)  # 2 minutes
    print("You have 2 minutes to finish up!")
    time.sleep(2)
elif mode == "move-limited":
    move_limit = 30
else:
    print("Invalid mode, defaulting to move-limited.")
    mode = "move-limited"

while True:
    if pressed_buttons == buttons_to_press:
        print("🎉 You pressed all the buttons! You win!")
        timer_event.set()
        break
    if moves_used >= move_limit:
        print("❌ Out of moves! Game over.")
        timer_event.set()
        break

    render_game_state()

    cmd = input("Move (e.g., 'north 3') or 'exit': ").lower()
    if cmd == "exit":
        timer_event.set()
        break
    try:
        direction, steps = cmd.split()
        steps = int(steps)
        if direction in DIRECTIONS:
            path = preview_path(direction, steps)
            if not path:
                print("🚫 Can't move that way!")
                continue

            render_game_state(path)
            confirm = input("Confirm move? (y/n): ").lower()
            if confirm == "y":
                move_player(path)
        else:
            print("Invalid direction. Try again.")
    except:
        print("Invalid command format. Use: direction steps (e.g., 'east 2').")
