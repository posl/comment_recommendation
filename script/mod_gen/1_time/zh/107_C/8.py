def solve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    #print(N, K, X)
    res = 10**9
    for i in range(N-K+1):
        #print(i, i+K-1)
        res = min(res, X[i+K-1]-X[i]+min(abs(X[i]), abs(X[i+K-1])))
    print(res)

if __name__ == '__main__':
    solve()