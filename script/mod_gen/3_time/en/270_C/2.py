def main():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
    dist = [0] * n
    dist[x] = 0
    q = [x]
    while q:
        v = q.pop()
        for to in edges[v]:
            if dist[to] == 0:
                dist[to] = dist[v] + 1
                q.append(to)
    for i in range(n):
        if i == x or i == y:
            continue
        if dist[i] > dist[y]:
            print(i + 1, end=' ')
    print(y + 1)

if __name__ == '__main__':
    main()