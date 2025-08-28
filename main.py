board = [

    [
    # Row 1
    {"name": "cell-1-1", "type": "start", "north": None,       "south": "cell-2-1", "east": "cell-1-2", "west": None},
    {"name": "cell-1-2", "type": "blank", "north": None,       "south": "cell-2-2", "east": "cell-1-3", "west": "cell-1-1"},
    {"name": "cell-1-3", "type": "blank", "north": None,       "south": "cell-2-3", "east": "cell-1-4", "west": "cell-1-2"},
    {"name": "cell-1-4", "type": "blank", "north": None,       "south": "cell-2-4", "east": "cell-1-5", "west": "cell-1-3"},
    {"name": "cell-1-5", "type": "blank", "north": None,       "south": "cell-2-5", "east": "cell-1-6", "west": "cell-1-4"},
    {"name": "cell-1-6", "type": "blank", "north": None,       "south": "cell-2-6", "east": None,       "west": "cell-1-5"},
    ],

    # Row 2
    [
    {"name": "cell-2-1", "type": "blank", "north": "cell-1-1", "south": "cell-3-1", "east": "cell-2-2", "west": None},
    {"name": "cell-2-2", "type": "blank", "north": "cell-1-2", "south": "cell-3-2", "east": "cell-2-3", "west": "cell-2-1"},
    {"name": "cell-2-3", "type": "spike", "north": "cell-1-3", "south": "cell-3-3", "east": "cell-2-4", "west": "cell-2-2"},
    {"name": "cell-2-4", "type": "button", "north": "cell-1-4", "south": "cell-3-4", "east": "cell-2-5", "west": "cell-2-3"},
    {"name": "cell-2-5", "type": "blank", "north": "cell-1-5", "south": "cell-3-5", "east": "cell-2-6", "west": "cell-2-4"},
    {"name": "cell-2-6", "type": "blank", "north": "cell-1-6", "south": "cell-3-6", "east": None,       "west": "cell-2-5"},
    ],
    [
    # Row 3
    {"name": "cell-3-1", "type": "button", "north": "cell-2-1", "south": "cell-4-1", "east": "cell-3-2", "west": None},
    {"name": "cell-3-2", "type": "blank", "north": "cell-2-2", "south": "cell-4-2", "east": "cell-3-3", "west": "cell-3-1"},
    {"name": "cell-3-3", "type": "blank", "north": "cell-2-3", "south": "cell-4-3", "east": "cell-3-4", "west": "cell-3-2"},
    {"name": "cell-3-4", "type": "blank", "north": "cell-2-4", "south": "cell-4-4", "east": "cell-3-5", "west": "cell-3-3"},
    {"name": "cell-3-5", "type": "blank", "north": "cell-2-5", "south": "cell-4-5", "east": "cell-3-6", "west": "cell-3-4"},
    {"name": "cell-3-6", "type": "blank", "north": "cell-2-6", "south": "cell-4-6", "east": None,       "west": "cell-3-5"},
    ],
    [
    # Row 4
    {"name": "cell-4-1", "type": "blank", "north": "cell-3-1", "south": "cell-5-1", "east": "cell-4-2", "west": None},
    {"name": "cell-4-2", "type": "blank", "north": "cell-3-2", "south": "cell-5-2", "east": "cell-4-3", "west": "cell-4-1"},
    {"name": "cell-4-3", "type": "blank", "north": "cell-3-3", "south": "cell-5-3", "east": "cell-4-4", "west": "cell-4-2"},
    {"name": "cell-4-4", "type": "blank", "north": "cell-3-4", "south": "cell-5-4", "east": "cell-4-5", "west": "cell-4-3"},
    {"name": "cell-4-5", "type": "blank", "north": "cell-3-5", "south": "cell-5-5", "east": "cell-4-6", "west": "cell-4-4"},
    {"name": "cell-4-6", "type": "blank", "north": "cell-3-6", "south": "cell-5-6", "east": None,       "west": "cell-4-5"},
    ],
    [
    # Row 5
    {"name": "cell-5-1", "type": "blank", "north": "cell-4-1", "south": "cell-6-1", "east": "cell-5-2", "west": None},
    {"name": "cell-5-2", "type": "wall", "north": "cell-4-2", "south": "cell-6-2", "east": "cell-5-3", "west": "cell-5-1"},
    {"name": "cell-5-3", "type": "blank", "north": "cell-4-3", "south": "cell-6-3", "east": "cell-5-4", "west": "cell-5-2"},
    {"name": "cell-5-4", "type": "blank", "north": "cell-4-4", "south": "cell-6-4", "east": "cell-5-5", "west": "cell-5-3"},
    {"name": "cell-5-5", "type": "blank", "north": "cell-4-5", "south": "cell-6-5", "east": "cell-5-6", "west": "cell-5-4"},
    {"name": "cell-5-6", "type": "button", "north": "cell-4-6", "south": "cell-6-6", "east": None,       "west": "cell-5-5"},
    ],
    [
    # Row 6
    {"name": "cell-6-1", "type": "blank", "north": "cell-5-1", "south": None,       "east": "cell-6-2", "west": None},
    {"name": "cell-6-2", "type": "button", "north": "cell-5-2", "south": None,       "east": "cell-6-3", "west": "cell-6-1"},
    {"name": "cell-6-3", "type": "blank", "north": "cell-5-3", "south": None,       "east": "cell-6-4", "west": "cell-6-2"},
    {"name": "cell-6-4", "type": "blank", "north": "cell-5-4", "south": None,       "east": "cell-6-5", "west": "cell-6-3"},
    {"name": "cell-6-5", "type": "blank", "north": "cell-5-5", "south": None,       "east": "cell-6-6", "west": "cell-6-4"},
    {"name": "cell-6-6", "type": "blank", "north": "cell-5-6", "south": None,       "east": None,       "west": "cell-6-5"}
    ]
]

# Directions (row, col deltas)
DIRECTIONS = {
    "north": (-1, 0), "south": (1, 0),
    "west": (0, -1), "east": (0, 1),
    "northwest": (-1, -1), "northeast": (-1, 1),
    "southwest": (1, -1), "southeast": (1, 1)
}

# Starting state
player_pos = (0, 0)  # row 0, col 0 ("cell-1-1")
buttons_to_press = {cell["name"] for row in board for cell in row if cell["type"] == "button"}
pressed_buttons = set()
move_limit = 15
moves_used = 0

#tutorial text
print("Welcome to the tutorial for A Chessish Game, a puzzle game with different objectives and obstacles. \n This game has you play as a chess piece, and currently, you are a queen (you can move any number of spaces in all eight directions). \n You may notice that certain spaces on the board have different names. \n The button spaces are your win condition: you must stand on each to win. \n The spike space will make you lose when stepped on. \n The wall space will stop your movement, and cannot be stepped on. Got that? \n Ok go wander into the wild good luck")

def get_cell(r, c):
    if 0 <= r < 6 and 0 <= c < 6:
        return board[r][c]
    return None

def print_mini_map(path=None):
    for r in range(6):
        row_str = ""
        for c in range(6):
            if path and (r, c) in path and (r, c) != player_pos:
                row_str += " * "  # highlight planned path
                continue
            cell = board[r][c]
            if (r, c) == player_pos:
                row_str += " P "
            elif cell["type"] == "wall":
                row_str += " # "
            elif cell["type"] == "spike":
                row_str += " X "
            elif cell["type"] == "button":
                if cell["name"] in pressed_buttons:
                    row_str += " b "  # pressed
                else:
                    row_str += " B "  # unpressed
            elif cell["type"] == "start":
                row_str += " S "
            else:
                row_str += " . "
        print(row_str)
    print()

def preview_path(direction, steps):
    """Return the path the player would take, stopping early if blocked."""
    dr, dc = DIRECTIONS[direction]
    r, c = player_pos
    path = []
    for _ in range(steps):
        r += dr
        c += dc
        cell = get_cell(r, c)
        if cell is None or cell["type"] == "wall":
            break  # stop pathing at edge or wall
        path.append((r, c))
    return path

def move_player(path):
    """Actually move the player along the chosen path."""
    global player_pos, pressed_buttons, moves_used
    for (r, c) in path:
        cell = get_cell(r, c)
        if cell["type"] == "spike":
            print(f"💀 You stepped on {cell['name']}... SPIKES! Game over.")
            exit()
        if cell["type"] == "button" and cell["name"] not in pressed_buttons:
            pressed_buttons.add(cell["name"])
            print(f"🔘 Pressed button at {cell['name']}!")
        player_pos = (r, c)
    moves_used += 1

# Game loop
while True:
    if pressed_buttons == buttons_to_press:
        print("🎉 You pressed all the buttons! You win!")
        break
    if moves_used >= move_limit:
        print("❌ Out of moves! Game over.")
        break

    print(f"\n📍 You are at {get_cell(*player_pos)['name']} ({get_cell(*player_pos)['type']})")
    print(f"Buttons pressed: {len(pressed_buttons)}/{len(buttons_to_press)} | Moves left: {move_limit - moves_used}")
    print_mini_map()

    cmd = input("Move (e.g., 'north 3') or 'exit': ").lower()
    if cmd == "exit":
        break
    try:
        direction, steps = cmd.split()
        steps = int(steps)
        if direction in DIRECTIONS:
            path = preview_path(direction, steps)
            if not path:
                print("🚫 Can't move that way!")
                continue
            print("Planned move path:")
            print_mini_map(path)
            confirm = input("Confirm move? (y/n): ").lower()
            if confirm == "y":
                move_player(path)
        else:
            print("Invalid direction. Try again.")
    except:
        print("Invalid command format. Use: direction steps (e.g., 'east 2').")
