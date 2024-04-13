def street_fighter_selection(fighters, initial_position, moves):
    # Define grid dimensions
    rows = len(fighters)
    cols = len(fighters[0])
    
    # Extract initial position coordinates
    current_row, current_col = initial_position
    
    # List to store hovered characters
    hovered_characters = []
    
    # Iterate through each move
    for move in moves:
        if move == 'up':
            # Move up if not in the top row
            if current_row > 0:
                current_row -= 1
        elif move == 'down':
            # Move down if not in the bottom row
            if current_row < rows - 1:
                current_row += 1
        elif move == 'left':
            # Move left with circular wrapping
            current_col = (current_col - 1) % cols
        elif move == 'right':
            # Move right with circular wrapping
            current_col = (current_col + 1) % cols
        
        # Add the character at the new position to the list
        hovered_characters.append(fighters[current_row][current_col])
    
    return hovered_characters
