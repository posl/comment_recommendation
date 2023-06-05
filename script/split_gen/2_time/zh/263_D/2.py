def dfs(n, m, a, i):
    if i == n:
        print(' '.join(map(str, a)))
    else:
        for j in range(1, m + 1):
            a[i] = j
            dfs(n, m, a, i + 1)
