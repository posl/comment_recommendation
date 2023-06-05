def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    if N >= M:
        print(0)
        return
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort(reverse=True)
    #print(diff)
    print(sum(diff[N-1:]))
solve()
