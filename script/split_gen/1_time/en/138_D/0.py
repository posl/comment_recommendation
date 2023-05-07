def main():
    N, Q = map(int, input().split())
    a = [0] * (N - 1)
    b = [0] * (N - 1)
    for i in range(N - 1):
        a[i], b[i] = map(int, input().split())
    p = [0] * Q
    x = [0] * Q
    for i in range(Q):
        p[i], x[i] = map(int, input().split())
    # 1-indexed array
    a = [0] + a
    b = [0] + b
    p = [0] + p
    x = [0] + x
    # adjacency list
    adj = [[] for _ in range(N + 1)]
    for i in range(1, N):
        adj[a[i]].append(b[i])
        adj[b[i]].append(a[i])
    # dfs
    visited = [False] * (N + 1)
    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    first = [0] * (N + 1)
    last = [0] * (N + 1)
    order = []
    def dfs(v, d):
        visited[v] = True
        depth[v] = d
        first[v] = len(order)
        order.append(v)
        for u in adj[v]:
            if visited[u]:
                continue
            parent[u] = v
            dfs(u, d + 1)
            order.append(v)
        last[v] = len(order) - 1
    dfs(1, 0)
    # segment tree
    st = [0] * (2 * N)
    def update(i, x):
        i += N
        st[i] += x
        while i > 1:
            i >>= 1
            st[i] = st[2 * i] + st[2 * i + 1]
    def query(l, r):
        l += N
        r += N
        s = 0
        while l < r:
            if l & 1:
                s += st[l]
                l += 1
            if r & 1:
                r -= 1
                s += st[r]
            l >>= 1
