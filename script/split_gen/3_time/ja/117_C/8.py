def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        return 0
    else:
        d = [X[i+1] - X[i] for i in range(M-1)]
        d.sort(reverse=True)
        return sum(d[N-1:])
    
print(solve())
