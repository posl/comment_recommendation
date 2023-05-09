def solve():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[False] * (y + 1) for _ in range(x + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if dp[j][k]:
                    dp[min(x, j + a[i])][min(y, k + b[i])] = True
    for i in range(x, -1, -1):
        for j in range(y, -1, -1):
            if dp[i][j]:
                print(i + j)
                return
    print(-1)
