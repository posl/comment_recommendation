def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    # print(grid)
    ans = []
    for i in range(W):
        tmp = 0
        for j in range(H):
            if grid[j][i] == "#":
                tmp += 1
        ans.append(tmp)
    print(" ".join(map(str, ans)))
