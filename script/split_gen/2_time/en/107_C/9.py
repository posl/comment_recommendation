def solve():
    N,K = map(int,input().split())
    X = list(map(int,input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        ans = min(ans,min(abs(X[i]),abs(X[i+K-1]))+abs(X[i+K-1]-X[i]))
    print(ans)
    return 0
