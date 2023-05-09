def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    depth = [0]*N
    parent = [0]*N
    q = deque([0])
    while q:
        v = q.popleft()
        for w in G[v]:
            if depth[w] == 0:
                depth[w] = depth[v] + 1
                parent[w] = v
                q.append(w)
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if depth[c] < depth[d]:
            c, d = d, c
        while depth[c] > depth[d]:
            c = parent[c]
        while c != d:
            c = parent[c]
            d = parent[d]
        if c == d:
            if depth[c] % 2 == 0:
                print("Town")
            else:
                print("Road")
