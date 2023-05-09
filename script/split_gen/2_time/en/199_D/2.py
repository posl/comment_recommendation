def main():
    N, M = map(int, input().split())
    edges = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a - 1].add(b - 1)
        edges[b - 1].add(a - 1)
    colors = [0] * N
    count = 0
    def dfs(v):
        nonlocal count
        if v == N:
            count += 1
            return
        for c in range(3):
            colors[v] = c
            if all(colors[v] != colors[u] for u in edges[v]):
                dfs(v + 1)
    dfs(0)
    print(count)
