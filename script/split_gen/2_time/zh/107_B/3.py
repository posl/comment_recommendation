def get_input():
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))
    return h, w, grid
