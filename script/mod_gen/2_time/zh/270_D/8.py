def game(N, K, A):
    A = [0] + A
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = 1
        for j in range(1, K + 1):
            if A[j] <= i:
                dp[i] = max(dp[i], 1 - dp[i - A[j]])
    return sum(dp)
N, K = map(int, input().split())
A = list(map(int, input().split()))
print(game(N, K, A))
