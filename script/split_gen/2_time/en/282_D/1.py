def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if not visited[i]:
            q = [i]
            visited[i] = True
            while q:
                v = q.pop()
                for next_v in graph[v]:
                    if not visited[next_v]:
                        q.append(next_v)
                        visited[next_v] = True
            ans += 1
    print(ans - 1)
