def f(n, a, x, y):
    ans = 0
    for i in range(2**n):
        honest = [0] * n
        for j in range(n):
            if (i >> j) & 1:
                honest[j] = 1
        ok = True
        for j in range(n):
            if honest[j] == 0:
                continue
            for k in range(a[j]):
                if honest[x[j][k] - 1] != y[j][k]:
                    ok = False
        if ok:
            ans = max(ans, sum(honest))
    return ans

if __name__ == '__main__':
    f()