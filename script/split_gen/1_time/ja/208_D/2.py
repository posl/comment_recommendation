def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    edges.sort(key=lambda x: x[2])
    ans = 0
    for i in range(m):
        a, b, c = edges[i]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(i):
            a2, b2, c2 = edges[j]
            dp[a2][b2] = c2
        for k in range(1, n + 1):
            for j in range(1, n + 1):
                for l in range(1, n + 1):
                    if dp[j][k] != 0 and dp[k][l] != 0:
                        if dp[j][l] == 0:
                            dp[j][l] = dp[j][k] + dp[k][l]
                        else:
                            dp[j][l] = min(dp[j][l], dp[j][k] + dp[k][l])
        for j in range(1, n + 1):
            if dp[j][a] != 0 and dp[j][b] != 0:
                ans += dp[j][a] + dp[j][b] + c
    print(ans)
