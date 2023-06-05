def get_path():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
    dist = [-1] * n
    dist[x] = 0
    que = [x]
    while que:
        v = que.pop()
        for nv in tree[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
    path = [y]
    v = y
    while v != x:
        for nv in tree[v]:
            if dist[nv] == dist[v] - 1:
                v = nv
                path.append(v)
                break
    path.reverse()
    return path

if __name__ == '__main__':
    get_path()