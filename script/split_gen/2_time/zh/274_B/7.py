def solve(h, w, c):
    ans = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = 1
    for i in range(h):
        for j in range(1, w):
            ans[i][j] += ans[i][j-1]
    for i in range(1, h):
        for j in range(w):
            ans[i][j] += ans[i-1][j]
    return ans
