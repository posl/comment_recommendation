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
    for i in range(2 ** N):
        honest = []
        for j in range(N):
            if ((i >> j) & 1):
                honest.append(j)
        flag = True
        for j in honest:
            for k in range(A[j]):
                if (((i >> (X[j][k] - 1)) & 1) ^ Y[j][k]):
                    flag = False
        if flag:
            ans = max(ans, len(honest))
    print(ans)
