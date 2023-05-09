def main():
    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))
    color = [-1] * n
    color[0] = 0
    que = [(0, 0)]
    while que:
        now, c = que.pop()
        for nxt, w in tree[now]:
            if color[nxt] == -1:
                color[nxt] = c ^ (w % 2)
                que.append((nxt, color[nxt]))
    print(*color, sep='
')

if __name__ == '__main__':
    main()