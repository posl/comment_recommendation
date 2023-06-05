def solve():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    minCost = 1000000000
    for i in range(N):
        if X[i] > 0:
            minCost = min(minCost, P[i])
    if minCost == 1000000000:
        print(-1)
    else:
        print(minCost)
