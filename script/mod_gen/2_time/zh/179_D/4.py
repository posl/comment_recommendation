def main():
    N,K = map(int,input().split())
    L = [0]*K
    R = [0]*K
    for i in range(K):
        L[i],R[i] = map(int,input().split())
    
    #print(N,K,L,R)
    #计算每个位置的方案数
    dp = [0]*(N+1)
    dp[1] = 1
    for i in range(1,N+1):
        for j in range(K):
            if i+L[j] <= N:
                dp[i+L[j]] += dp[i]
                dp[i+L[j]] %= 998244353
            if i+R[j]+1 <= N:
                dp[i+R[j]+1] -= dp[i]
                dp[i+R[j]+1] %= 998244353
    #print(dp)
    print(dp[N])

if __name__ == '__main__':
    main()