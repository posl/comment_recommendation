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
    for i in range(1 << N):
        honest = []
        for j in range(N):
            if i >> j & 1:
                honest.append(j)
        flag = True
        for j in range(len(honest)):
            for k in range(A[honest[j]]):
                if Y[honest[j]][k] == 1 and X[honest[j]][k] not in honest:
                    flag = False
                if Y[honest[j]][k] == 0 and X[honest[j]][k] in honest:
                    flag = False
        if flag:
            ans = max(ans, len(honest))
    print(ans)

if __name__ == '__main__':
    main()