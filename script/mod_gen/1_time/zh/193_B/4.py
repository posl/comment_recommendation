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
    min_price = -1
    for i in range(N):
        if X[i] > 0:
            if min_price == -1:
                min_price = P[i]
            else:
                min_price = min(min_price, P[i])
    print(min_price)

if __name__ == '__main__':
    main()