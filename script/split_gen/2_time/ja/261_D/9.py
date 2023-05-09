def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    bonus = []
    for _ in range(M):
        C, Y = map(int, input().split())
        bonus.append((C, Y))
    bonus.sort(reverse=True)
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for C, Y in bonus:
            if i + 1 >= C:
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - C] + Y)
    print(dp[N])
