def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    colors = [0] * n
    colors[0] = 1
    q = [0]
    while q:
        cur = q.pop()
        for nxt in g[cur]:
            if colors[nxt] == 0:
                colors[nxt] = -colors[cur]
                q.append(nxt)
            elif colors[nxt] == colors[cur]:
                print(0)
                exit()
    cnt = sum(c == 1 for c in colors)
    print(cnt * (n - cnt) - m)

if __name__ == '__main__':
    main()