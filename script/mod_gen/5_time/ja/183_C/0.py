def dfs(now, visited, dist, K, N):
    if len(visited) == N:
        if dist + T[now][0] == K:
            return 1
        else:
            return 0
    ret = 0
    for i in range(N):
        if i in visited:
            continue
        ret += dfs(i, visited + [i], dist + T[now][i], K, N)
    return ret
N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
print(dfs(0, [0], 0, K, N))

if __name__ == '__main__':
    dfs()