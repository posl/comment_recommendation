def main():
    N = int(input())
    W = list(map(int,input().split()))
    S = sum(W)
    dp = [[0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S+1):
            if j >= W[i]:
                dp[i+1][j] = max(dp[i][j-W[i]],dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]
    ans = 10**9
    for i in range(S+1):
        if dp[N][i]:
            ans = min(ans,abs(S-2*i))
    print(ans)
main()
