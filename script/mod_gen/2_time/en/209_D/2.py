def main():
    N, Q = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for w in edges[v]:
            if depth[w] == -1:
                depth[w] = depth[v] + 1
                stack.append(w)
    for _ in range(Q):
        c, d = map(int, input().split())
        if (depth[c - 1] + depth[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    main()