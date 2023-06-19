def solve():
    from math import gcd
    from collections import Counter
    N,X=map(int,input().split())
    A=[list(map(int,input().split())) for _ in range(N)]
    L=[a[0] for a in A]
    C=[a[1:] for a in A]
    D=[Counter() for _ in range(N)]
    for i in range(N):
        for j in range(L[i]):
            D[i][C[i][j]]+=1
    E=[Counter() for _ in range(N)]
    E[0]=D[0]
    for i in range(1,N):
        for k,v in E[i-1].items():
            for j in range(L[i]):
                g=gcd(k,C[i][j])
                E[i][g]+=v*D[i][C[i][j]]
    ans=0
    for k,v in E[N-1].items():
        if X%k==0 and X//k in E[N-1]:
            ans+=v*E[N-1][X//k]
    print(ans)
solve()
I solved this problem using the Chinese Remainder Theorem. The solution is here.
I solved this problem using a DP. Th
