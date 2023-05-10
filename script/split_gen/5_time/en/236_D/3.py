def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    dp = [[0 for _ in range(1 << n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dp[i][1 << i | 1 << j] = a[i][j]
    for i in range(1 << n):
        for j in range(n):
            if not i & 1 << j:
                continue
            for k in range(j + 1, n):
                if not i & 1 << k:
                    continue
                dp[k][i] = max(dp[k][i], dp[j][i ^ 1 << k] + a[j][k])
    print(dp[n - 1][(1 << n) - 1])
    return
