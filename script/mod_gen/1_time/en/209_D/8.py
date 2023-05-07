def main():
    import sys
    N, Q = map(int, sys.stdin.readline().split())
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                stack.append(u)
    for _ in range(Q):
        c, d = map(int, sys.stdin.readline().split())
        c, d = c-1, d-1
        if depth[c] % 2 == depth[d] % 2:
            print("Town")
        else:
            print("Road")
main()

if __name__ == '__main__':
    main()