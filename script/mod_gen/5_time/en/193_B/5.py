def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        A_i, P_i, X_i = input().split()
        A.append(int(A_i))
        P.append(int(P_i))
        X.append(int(X_i))
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