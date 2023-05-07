def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    min_price = 1000000001
    for i in range(N):
        if X[i] - A[i] > 0:
            if min_price > P[i]:
                min_price = P[i]
    if min_price == 1000000001:
        print(-1)
    else:
        print(min_price)
