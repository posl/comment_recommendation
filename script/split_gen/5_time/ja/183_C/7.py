def dfs(now, visited, weight):
    if len(visited) == N:
        if weight == K:
            return 1
        else:
            return 0
    else:
        ret = 0
        for i in range(N):
            if i in visited:
                continue
            else:
                visited.add(i)
                ret += dfs(i, visited, weight + T[now][i])
                visited.remove(i)
        return ret
N, K = map(int, input().split())
T = []
for _ in range(N):
    T.append(list(map(int, input().split())))
visited = set()
visited.add(0)
print(dfs(0, visited, 0))
