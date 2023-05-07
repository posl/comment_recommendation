def main():
    N,K = map(int,input().split())
    L = []
    R = []
    for _ in range(K):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    mod = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = -1
    for i in range(1,N):
        dp[i+1] = (dp[i+1] + dp[i]) % mod
        for j in range(K):
            dp[i+L[j]] = (dp[i+L[j]] + dp[i]) % mod
            dp[i+R[j]+1] = (dp[i+R[j]+1] - dp[i]) % mod
    for i in range(N):
        dp[i+1] = (dp[i+1] + dp[i]) % mod
    print(dp[N])
