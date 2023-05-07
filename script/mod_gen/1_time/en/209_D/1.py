def main():
    n, q = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    depth = [-1] * n
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edges[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                stack.append(u)
    for _ in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (depth[c] + depth[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')

if __name__ == '__main__':
    main()