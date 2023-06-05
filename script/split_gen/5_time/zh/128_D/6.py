def solve():
    N,K = map(int,input().split())
    V = list(map(int,input().split()))
    ans = 0
    for i in range(min(N,K)+1):
        for j in range(min(N-i,K-i)+1):
            #print(i,j)
            v = V[:i]+V[N-j:]
            v.sort()
            for k in range(K-i-j):
                if k < len(v) and v[k] < 0:
                    v[k] = 0
            ans = max(ans,sum(v))
    print(ans)
