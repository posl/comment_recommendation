def solve():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    colors = [0] * (N + 1)
    for i in range(1, N + 1):
        colors[i] = set(range(1, 4)) - set([colors[j] for j in graph[i]])
    ans = 1
    for i in range(1, N + 1):
        ans *= len(colors[i])
    print(ans)
solve()

if __name__ == '__main__':
    solve()