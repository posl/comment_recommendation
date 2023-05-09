def main():
    N, Q = map(int, input().split())
    AB = []
    for i in range(N - 1):
        AB.append(list(map(int, input().split())))
    CD = []
    for i in range(Q):
        CD.append(list(map(int, input().split())))
    edges = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = AB[i]
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    depth = [0] * N
    parent = [0] * N
    parent[0] = -1
    q = [0]
    while len(q) > 0:
        v = q.pop()
        for i in edges[v]:
            if depth[i] == 0:
                depth[i] = depth[v] + 1
                parent[i] = v
                q.append(i)
    for c, d in CD:
        c -= 1
        d -= 1
        if (depth[c] + depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")
