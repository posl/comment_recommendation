def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    matchsticks = [2,5,5,4,5,6,3,7,6]
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for a in A:
            if i + matchsticks[a - 1] > N:
                continue
            dp[i + matchsticks[a - 1]] = max(dp[i + matchsticks[a - 1]], dp[i] * 10 + a)
    print(dp[N])
