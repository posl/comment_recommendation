def main():
    N, Q = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for e in edges[v]:
            if depth[e] != -1:
                continue
            depth[e] = depth[v] + 1
            stack.append(e)
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (depth[c] + depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    main()