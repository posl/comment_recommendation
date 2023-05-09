def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    visited = [False for _ in range(n)]
    cnt = 0
    for i in range(n):
        if visited[i]:
            continue
        cnt += 1
        visited[i] = True
        q = [i]
        while q:
            v = q.pop()
            for u in g[v]:
                if visited[u]:
                    continue
                visited[u] = True
                q.append(u)
    print(cnt)

if __name__ == '__main__':
    main()