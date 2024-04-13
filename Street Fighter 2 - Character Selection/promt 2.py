def simulate_character_selection(fighters, initial_position, moves):
    rows = len(fighters)
    cols = len(fighters[0])
    result = []

    # Initial cursor position
    row, col = initial_position

    for move in moves:
        if move == 'up':
            row = max(0, row - 1)  # Ensure we don't go above the top row
        elif move == 'down':
            row = min(rows - 1, row + 1)  # Ensure we don't go below the bottom row
        elif move == 'left':
            col = (col - 1) % cols  # Circular movement for left direction
        elif move == 'right':
            col = (col + 1) % cols  # Circular movement for right direction

        result.append(fighters[row][col])

    return result