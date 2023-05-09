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
    min_price = 10**18
    for i in range(N):
        if A[i] < X[i]:
            min_price = min(min_price, P[i])
    if min_price == 10**18:
        print(-1)
    else:
        print(min_price)

if __name__ == '__main__':
    main()