def main():
    N,K,D = map(int,input().split())
    a = list(map(int,input().split()))
    #print(N,K,D,a)
    #N,K,D = 4,2,2
    #a = [1,2,3,4]
    if K == 1:
        print(a[0]%D)
    else:
        #print("else")
        dp = [0]*(N+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,N+1):
            dp[i] = dp[i-1]*i
        #print(dp)
        ans = 0
        for i in range(1,N-K+2):
            ans += (dp[i+K-2]//dp[i-1]//dp[K-1])*(sum(a[i-1:i+K-1])%D)
        print(ans%D)
