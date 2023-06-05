def solve():
    N,K,D=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    S=[0]*(N+1)
    for i in range(1,N+1):
        S[i]=S[i-1]+A[i-1]
    dp=[[0]*(S[-1]+1) for _ in range(K+1)]
    for i in range(1,K+1):
        for j in range(1,S[-1]+1):
            for k in range(1,D+1):
                if j-k>=0:
                    dp[i][j]=max(dp[i][j],dp[i-1][j-k]+A[k-1])
    print(dp[-1][-1])
