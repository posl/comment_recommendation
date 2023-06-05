def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    sumA = sum(A)
    dp = [[0 for _ in range(sumA+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(sumA+1):
            if j-A[i]>=0:
                dp[i+1][j] = (dp[i][j]+dp[i][j-A[i]])%mod
            else:
                dp[i+1][j] = dp[i][j]
    ans = 0
    for i in range(1, sumA+1):
        if i%N==0:
            ans = (ans+dp[N][i])%mod
    print(ans)

if __name__ == '__main__':
    main()