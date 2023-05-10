def main():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        x = []
        y = []
        for j in range(A[i]):
            xj, yj = map(int, input().split())
            x.append(xj)
            y.append(yj)
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(2**N):
        honest = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if Y[j][k] == 1 and (i >> (X[j][k] - 1)) & 1 == 0:
                        honest = False
            else:
                for k in range(A[j]):
                    if Y[j][k] == 0 and (i >> (X[j][k] - 1)) & 1 == 1:
                        honest = False
        if honest:
            ans = max(ans, bin(i).count("1"))
    print(ans)

if __name__ == '__main__':
    main()