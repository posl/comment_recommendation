def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        return 0
    else:
        Y = []
        for i in range(M-1):
            Y.append(X[i+1]-X[i])
        Y.sort()
        return sum(Y[:M-N])
print(solve())
