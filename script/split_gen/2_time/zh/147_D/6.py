def solve():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        a = int(input())
        A.append(a)
        x = []
        y = []
        for j in range(a):
            x_y = input().split()
            x.append(int(x_y[0]))
            y.append(int(x_y[1]))
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(2 ** N):
        honest = []
        dishonest = []
        for j in range(N):
            if (i >> j) & 1:
                honest.append(j + 1)
            else:
                dishonest.append(j + 1)
        flag = True
        for j in range(len(honest)):
            for k in range(A[honest[j] - 1]):
                if Y[honest[j] - 1][k] == 1 and X[honest[j] - 1][k] not in honest:
                    flag = False
                if Y[honest[j] - 1][k] == 0 and X[honest[j] - 1][k] not in dishonest:
                    flag = False
        if flag:
            ans = max(ans, len(honest))
    print(ans)
