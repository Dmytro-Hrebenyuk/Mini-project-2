def next_gen(cells):
    def count_neighbors(cells, row, col):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i != row or j != col) and 0 <= i < len(cells) and 0 <= j < len(cells[0]):
                    count += cells[i][j]
        return count

    def apply_rules(cells):
        new_cells = [[0] * len(cells[0]) for _ in range(len(cells))]
        for i in range(len(cells)):
            for j in range(len(cells[0])):
                live_neighbors = count_neighbors(cells, i, j)
                if cells[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_cells[i][j] = 0
                    else:
                        new_cells[i][j] = 1
                elif cells[i][j] == 0 and live_neighbors == 3:
                    new_cells[i][j] = 1
        return new_cells

    return apply_rules(cells)
