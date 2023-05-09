def main():
    N = int(input())
    A = []
    P = []
    X = []
    for n in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    min_price = 10 ** 9 + 1
    for n in range(N):
        if X[n] - A[n] > 0:
            min_price = min(min_price, P[n])
    if min_price == 10 ** 9 + 1:
        print(-1)
    else:
        print(min_price)

if __name__ == '__main__':
    main()