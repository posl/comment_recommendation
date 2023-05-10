def check_rows(grid):
    for row in grid:
        if row.count('#') >= 6:
            return True
    return False

if __name__ == '__main__':
    check_rows()