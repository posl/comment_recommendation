def solve():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        x = []
        y = []
        for j in range(A[i]):
            tmp = input().split()
            x.append(int(tmp[0]))
            y.append(int(tmp[1]))
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(2**N):
        honest = [False] * N
        tmp = i
        for j in range(N):
            if tmp % 2 == 1:
                honest[N-1-j] = True
            tmp //= 2
        flag = True
        for j in range(N):
            if honest[j]:
                for k in range(A[j]):
                    if honest[X[j][k]-1] != bool(Y[j][k]):
                        flag = False
        if flag:
            ans = max(ans, sum(honest))
    print(ans)
