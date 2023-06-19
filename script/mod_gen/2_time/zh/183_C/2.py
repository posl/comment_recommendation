def dfs(city, time, visited, K):
    global ans
    if len(visited) == N:
        if time + T[city][0] == K:
            ans += 1
        return
    for i in range(N):
        if i not in visited:
            visited.add(i)
            dfs(i, time + T[city][i], visited, K)
            visited.remove(i)
    return
N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = set()
visited.add(0)
dfs(0, 0, visited, K)
print(ans)

if __name__ == '__main__':
    dfs()