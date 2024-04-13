# Код згенерований чатом
def simulate_character_selection(fighters, initial_position, moves):
    rows = len(fighters)
    cols = len(fighters[0])
    current_row, current_col = initial_position
    hovered_characters = []

    for move in moves:
        if move == 'up':
            current_row = max(0, current_row - 1)
        elif move == 'down':
            current_row = min(rows - 1, current_row + 1)
        elif move == 'left':
            current_col = (current_col - 1) % cols
        elif move == 'right':
            current_col = (current_col + 1) % cols

        hovered_characters.append(fighters[current_row][current_col])

    return hovered_characters

# оптимізованіший варіант коду , зроблений через словник

def street_fighter_selection(fighters, initial_position, moves):
    rows = len(fighters)
    cols = len(fighters[0])
    current_position = initial_position
    hovered_characters = []

    move_dict = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

    for move in moves:
        row, col = current_position
        move_row, move_col = move_dict[move]
        
        row = max(0, min(rows - 1, row + move_row))
        col = (col + move_col) % cols

        current_position = (row, col)
        hovered_characters.append(fighters[row][col])

    return hovered_characters
