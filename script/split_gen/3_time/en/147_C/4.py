def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = []
    Y = []
    for i in range(N):
        x = []
        y = []
        for _ in range(A[i]):
            x_i, y_i = map(int, input().split())
            x.append(x_i)
            y.append(y_i)
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(1 << N):
        ok = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if Y[j][k] == 1:
                        if (i >> (X[j][k] - 1)) & 1 == 0:
                            ok = False
                    else:
                        if (i >> (X[j][k] - 1)) & 1 == 1:
                            ok = False
        if ok:
            ans = max(ans, bin(i).count('1'))
    print(ans)
