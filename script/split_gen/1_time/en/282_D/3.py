def main():
    N, M = map(int, input().split())
    graph = {i: set() for i in range(1, N+1)}
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    ans = 0
    for i in range(1, N):
        for j in range(i+1, N+1):
            if j not in graph[i]:
                if len(graph[i] & graph[j]) == 0:
                    ans += 1
    print(ans)
