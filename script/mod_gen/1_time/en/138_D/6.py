def main():
    n, q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    queries = [list(map(int, input().split())) for _ in range(q)]
    g = [[] for _ in range(n + 1)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    visited = [False] * (n + 1)
    visited[1] = True
    depth = [0] * (n + 1)
    parent = [0] * (n + 1)
    stack = [1]
    while stack:
        v = stack.pop()
        for u in g[v]:
            if visited[u]:
                continue
            visited[u] = True
            parent[u] = v
            depth[u] = depth[v] + 1
            stack.append(u)
    children = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        children[parent[i]].append(i)
    idx = [0] * (n + 1)
    cnt = 0
    stack = [1]
    while stack:
        v = stack.pop()
        cnt += 1
        idx[v] = cnt
        for u in children[v]:
            stack.append(u)
    a = [0] * (n + 1)
    for p, x in queries:
        a[idx[p]] += x
        if idx[p] + len(children[p]) <= n:
            a[idx[p] + len(children[p])] -= x
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    print(*a[1:])
main()

if __name__ == '__main__':
    main()