def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for j in A:
            if i - j >= 0 and dp[i-j] != -1:
                dp[i] = max(dp[i], dp[i-j] * 10 + j)
    print(dp[-1])
