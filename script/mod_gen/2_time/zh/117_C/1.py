def solution():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    else:
        X_diff = []
        for i in range(M-1):
            X_diff.append(X[i+1]-X[i])
        X_diff.sort(reverse=True)
        print(sum(X_diff[N-1:]))
        return
solution()
