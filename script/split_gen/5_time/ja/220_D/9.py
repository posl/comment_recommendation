def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * (N + 1)
        dp[0] = 1
        for j in range(N):
            if dp[j] == 0:
                continue
            if j >= 2:
                dp[j] = (dp[j] + dp[j - 2]) % mod
            if j <= N - 2:
                dp[j + 2] = (dp[j + 2] + dp[j]) % mod
        for j in range(N):
            if A[j] == i:
                ans[i] = (ans[i] + dp[j]) % mod
    for i in range(10):
        print(ans[i])
