def get_grid():
    grid = []
    while True:
        try:
            row = input()
            grid.append(row)
        except EOFError:
            break
    return grid
