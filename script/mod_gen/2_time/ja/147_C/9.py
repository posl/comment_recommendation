def dfs(N, A, x, y, honest, i):
    if i == N:
        for j in range(N):
            for k in range(A[j]):
                if honest[j] != honest[x[j][k] - 1] == y[j][k]:
                    return 0
        return honest.count(1)
    honest[i] = 1
    res = dfs(N, A, x, y, honest, i + 1)
    honest[i] = 0
    res = max(res, dfs(N, A, x, y, honest, i + 1))
    return res

if __name__ == '__main__':
    dfs()