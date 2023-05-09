def main():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        edge[a].append(b)
        edge[b].append(a)
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if depth[u] != -1:
                continue
            depth[u] = depth[v] + 1
            stack.append(u)
    for _ in range(Q):
        c, d = map(int, input().split())
        c, d = c-1, d-1
        if (depth[c] + depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    main()