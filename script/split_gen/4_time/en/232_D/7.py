def get_input():
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(input())
    return grid
