def solve():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = list(map(int, input().split()))
        A.append(a)
        P.append(p)
        X.append(x)
    min_price = 1000000000
    for i in range(N):
        if X[i] > 0:
            min_price = min(min_price, P[i])
    if min_price == 1000000000:
        print(-1)
    else:
        print(min_price)
