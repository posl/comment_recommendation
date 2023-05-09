def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)
seen = [False] * N
ans = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    ans += 1
print(ans)

if __name__ == '__main__':
    dfs()