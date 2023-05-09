def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [0] * (N+1)
    for i in range(N+1):
        if i == 0:
            dp[i] = 0
        else:
            for j in range(M):
                if i - A[j] < 0:
                    continue
                dp[i] = max(dp[i], dp[i-A[j]]*10 + A[j])
    print(dp[N])
