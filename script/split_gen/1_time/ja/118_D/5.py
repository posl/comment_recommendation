def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [0] * (N + 1)
    for i in range(N + 1):
        for a in A:
            if i + a <= N:
                dp[i + a] = max(dp[i + a], dp[i] * 10 + a)
    print(dp[N])
