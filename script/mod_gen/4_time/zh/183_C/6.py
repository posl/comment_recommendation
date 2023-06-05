def dfs(now, visited, cost):
    global ans, N, K, T
    visited = visited | (1 << now)
    if visited == (1 << N) - 1 and cost + T[now][0] == K:
        ans += 1
    else:
        for i in range(N):
            if not visited & (1 << i):
                dfs(i, visited, cost + T[now][i])
N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, 0, 0)
print(ans)

if __name__ == '__main__':
    dfs()