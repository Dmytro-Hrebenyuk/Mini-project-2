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
