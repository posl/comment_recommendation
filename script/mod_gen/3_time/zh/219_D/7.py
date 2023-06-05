def solve():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[False for _ in range(y + 1)] for _ in range(x + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if dp[j][k]:
                    dp[min(x, j + a[i])][min(y, k + b[i])] = True
    ans = 10 ** 18
    for i in range(x, y + 1):
        for j in range(y, y + 1):
            if dp[i][j]:
                ans = min(ans, i + j)
    print(ans if ans != 10 ** 18 else -1)
solve()
