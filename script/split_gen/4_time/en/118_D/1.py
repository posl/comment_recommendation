def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(M):
            if i - A[j] >= 0:
                dp[i] = max(dp[i], dp[i - A[j]] + 1)
    ans = [0] * dp[N]
    for i in range(dp[N]):
        for j in range(M):
            if N - A[j] >= 0 and dp[N - A[j]] == dp[N] - i - 1:
                ans[i] = str(A[j])
                N -= A[j]
                break
    print(''.join(ans))
