def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x: x[1])
    dp = [0] * (n+1)
    dp[1] = 1
    for a, b in ab:
        if b == n:
            break
        dp[b] = (dp[a] + dp[b]) % (10**9+7)
    print(dp[n])
