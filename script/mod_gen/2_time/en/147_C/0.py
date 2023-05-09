def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    X = []
    Y = []
    for i in range(N):
        x = []
        y = []
        for j in range(A[i]):
            xi, yi = map(int, input().split())
            x.append(xi)
            y.append(yi)
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if Y[j][k] == 1 and X[j][k] != (i >> (X[j][k] - 1)) & 1 + 1:
                        flag = False
                        break
                    if Y[j][k] == 0 and X[j][k] == (i >> (X[j][k] - 1)) & 1 + 1:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)

if __name__ == '__main__':
    main()