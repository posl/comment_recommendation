def problems274b():
    H,W = map(int,input().split())
    s = [input() for i in range(H)]
    ans = [0]*W
    for i in range(H):
        for j in range(W):
            if s[i][j] == '#':
                ans[j] += 1
    print(*ans)
