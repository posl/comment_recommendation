def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    from collections import deque
    q = deque([0])
    color = [-1] * n
    color[0] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
    cnt = [0] * 2
    for c in color:
        cnt[c] += 1
    print(cnt[0] * cnt[1] - m)

if __name__ == '__main__':
    main()