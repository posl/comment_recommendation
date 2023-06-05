def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [[0] * 10 for _ in range(N)]
        for j in range(10):
            if i == A[0]:
                dp[0][j] = 1
            else:
                dp[0][j] = 0
        for j in range(1, N):
            for k in range(10):
                if k == A[j]:
                    dp[j][k] = sum(dp[j - 1]) % mod
                else:
                    dp[j][k] = dp[j - 1][k]
        ans[i] = sum(dp[-1]) % mod
    print('\n'.join(map(str, ans)))
