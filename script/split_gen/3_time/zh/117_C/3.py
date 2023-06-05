def solution():
    import sys
    import bisect
    N, M = map(int, sys.stdin.readline().strip().split())
    X = list(map(int, sys.stdin.readline().strip().split()))
    X.sort()
    X.append(X[0])
    ans = 0
    for i in range(M):
        if X[i] < 0 < X[i+1]:
            ans += min(-X[i], X[i+1])*2 + max(-X[i], X[i+1])
        else:
            ans += max(X[i], X[i+1]) - min(X[i], X[i+1])
    print(ans)
