def solve():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    ans = [0] * W
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                ans[j] += 1
    print(' '.join(map(str, ans)))
