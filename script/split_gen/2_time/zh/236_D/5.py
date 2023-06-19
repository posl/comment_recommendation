def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            dp[j][1 << i | 1 << j] = a[i][j]
    for s in range(1 << n):
        bits = [i for i in range(n) if s >> i & 1]
        m = len(bits)
        for i in range(m):
            for j in range(i + 1, m):
                p = bits[i]
                q = bits[j]
                dp[q][s | 1 << q] = max(dp[q][s | 1 << q], dp[p][s] + a[p][q])
    print(dp[n - 1][-1])
