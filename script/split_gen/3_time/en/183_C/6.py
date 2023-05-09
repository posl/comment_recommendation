def dfs(i, visited, total, N, K, T):
    if len(visited) == N:
        if total == K:
            return 1
        else:
            return 0
    else:
        ret = 0
        for j in range(N):
            if not j in visited:
                ret += dfs(j, visited + [j], total + T[i][j], N, K, T)
        return ret
