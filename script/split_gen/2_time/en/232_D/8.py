def main():
    # input
    H, W = map(int, input().split())
    # print(H, W)
    grid = []
    for i in range(H):
        grid.append(list(input()))
    # print(grid)
    # output
    print(visit(H, W, grid))
