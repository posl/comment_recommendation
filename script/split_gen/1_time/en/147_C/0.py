def main():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        X.append([])
        Y.append([])
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x)
            Y[i].append(y)
    ans = 0
    for i in range(2 ** N):
        honest = [0] * N
        for j in range(N):
            if (i >> j) & 1:
                honest[j] = 1
        ok = True
        for j in range(N):
            if honest[j] == 0:
                continue
            for k in range(A[j]):
                if honest[X[j][k] - 1] != Y[j][k]:
                    ok = False
        if ok:
            ans = max(ans, sum(honest))
    print(ans)
