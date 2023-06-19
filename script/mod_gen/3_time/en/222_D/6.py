def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(B[i], A[i] - 1, -1):
            dp[i + 1] += dp[j]
            dp[i + 1] %= mod
    print(dp[N])
main()
