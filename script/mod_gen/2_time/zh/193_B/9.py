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
    min_price = 10**9
    for i in range(N):
        if X[i] > 0:
            min_price = min(min_price, P[i])
    if min_price == 10**9:
        print(-1)
    else:
        print(min_price)

if __name__ == '__main__':
    main()