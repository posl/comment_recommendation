def dfs(A, N, M, i):
    if i == N:
        print(' '.join(map(str, A)))
        return
    for j in range(1, M+1):
        if i == 0 or A[i-1] < j:
            A[i] = j
            dfs(A, N, M, i+1)
