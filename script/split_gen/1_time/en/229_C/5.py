def main():
    N, W = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort()
    dp = [0] * (W + 1)
    for a, b in AB:
        for i in range(W, 0, -1):
            if i >= b:
                dp[i] = max(dp[i], dp[i - b] + a * b)
            else:
                dp[i] = max(dp[i], dp[i - 1] + a * i)
    print(dp[W])
