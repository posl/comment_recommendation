def solve():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = [int(i) for i in input().split()]
        A.append(a)
        P.append(p)
        X.append(x)
    min_price = float('inf')
    for i in range(N):
        if X[i] > 0:
            if min_price > P[i]:
                min_price = P[i]
    if min_price == float('inf'):
        min_price = -1
    print(min_price)
