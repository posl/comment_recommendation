def get_input():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(list(input()))
    return H, W, grid

if __name__ == '__main__':
    get_input()