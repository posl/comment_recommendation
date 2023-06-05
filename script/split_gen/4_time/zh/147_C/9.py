def func():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        x.append([0] * a[i])
        y.append([0] * a[i])
        for j in range(a[i]):
            x[i][j], y[i][j] = map(int, input().split())
    ans = 0
    for i in range(2 ** n):
        honest = [0] * n
        flag = 1
        for j in range(n):
            if (i >> j) & 1:
                honest[j] = 1
        for j in range(n):
            if honest[j]:
                for k in range(a[j]):
                    if honest[x[j][k] - 1] != y[j][k]:
                        flag = 0
        if flag:
            ans = max(ans, sum(honest))
    print(ans)
