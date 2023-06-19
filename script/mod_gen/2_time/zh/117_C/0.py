def solve():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()
    #print(X)
    if N >= M:
        print(0)
        return
    #print(X)
    d = []
    for i in range(M-1):
        d.append(X[i+1] - X[i])
    #print(d)
    d.sort()
    #print(d)
    ans = 0
    for i in range(M-N):
        ans += d[i]
    print(ans)
    return

if __name__ == '__main__':
    solve()