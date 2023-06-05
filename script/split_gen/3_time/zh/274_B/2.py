def problems274_b():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    ans = [0]*w
    for j in range(w):
        for i in range(h):
            if c[i][j] == '#':
                ans[j] += 1
    print(*ans)
