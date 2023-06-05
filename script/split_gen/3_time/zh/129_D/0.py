def get_max_lighted_cells(rows, cols, grid):
    max_lighted_cells = 0
    for row in range(rows):
        for col in range(cols):
            lighted_cells = 0
            lighted_cells += get_lighted_cells_in_direction(row, col, rows, cols, grid, -1, 0)
            lighted_cells += get_lighted_cells_in_direction(row, col, rows, cols, grid, 1, 0)
            lighted_cells += get_lighted_cells_in_direction(row, col, rows, cols, grid, 0, -1)
            lighted_cells += get_lighted_cells_in_direction(row, col, rows, cols, grid, 0, 1)
            if lighted_cells > max_lighted_cells:
                max_lighted_cells = lighted_cells
    return max_lighted_cells
