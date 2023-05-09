def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == ".":
                ans += 1
    print(ans)
