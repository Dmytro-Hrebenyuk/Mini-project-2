def next_gen(cells):
    # Function to count live neighbors of a cell
    def count_live_neighbors(row, col):
        live_count = 0
        for i in range(max(0, row - 1), min(len(cells), row + 2)):
            for j in range(max(0, col - 1), min(len(cells[0]), col + 2)):
                if (i, j) != (row, col) and cells[i][j] == 1:
                    live_count += 1
        return live_count

    # Create a new grid to store the next generation of cells
    next_generation = [[0] * len(cells[0]) for _ in range(len(cells))]

    # Iterate through each cell in the grid
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            live_neighbors = count_live_neighbors(i, j)
            
            # Apply the rules of the Game of Life
            if cells[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    next_generation[i][j] = 0  # Cell dies due to underpopulation or overpopulation
                else:
                    next_generation[i][j] = 1  # Cell survives to the next generation
            elif cells[i][j] == 0 and live_neighbors == 3:
                next_generation[i][j] = 1  # Dead cell becomes alive due to reproduction

    return next_generation
