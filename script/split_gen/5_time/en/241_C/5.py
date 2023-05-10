def check_rows(grid):
    for row in grid:
        if row.count('#') >= 6:
            return True
    return False
