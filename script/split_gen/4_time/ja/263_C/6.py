def dfs(i, n, m, a):
    if i == n:
        print(' '.join(map(str, a)))
        return
    for j in range(1, m+1):
        if i == 0:
            a[i] = j
            dfs(i+1, n, m, a)
        else:
            if a[i-1] < j:
                a[i] = j
                dfs(i+1, n, m, a)
