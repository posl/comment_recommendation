def main():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if depth[nv] == -1:
                depth[nv] = depth[v] + 1
                stack.append(nv)
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (depth[c] + depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")
