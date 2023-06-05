def dfs(N, M, arr, i, j):
    if i == N:
        print(' '.join(map(str, arr)))
        return
    for k in range(j+1, M+1):
        arr[i] = k
        dfs(N, M, arr, i+1, k)
