def next_gen(cells):
    def count_live_neighbors(cells, row, col):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i != row or j != col) and 0 <= i < len(cells) and 0 <= j < len(cells[0]) and cells[i][j] == 1:
                    count += 1
        return count

    def apply_rules(current_state, next_state):
        for i in range(len(current_state)):
            for j in range(len(current_state[0])):
                live_neighbors = count_live_neighbors(current_state, i, j)
                if current_state[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        next_state[i][j] = 0
                elif live_neighbors == 3:
                    next_state[i][j] = 1

    # Initialize the next state as a matrix of zeros with the same dimensions as the current state
    next_state = [[0] * len(cells[0]) for _ in range(len(cells))]

    # Apply the rules to generate the next state
    apply_rules(cells, next_state)

    return next_state
