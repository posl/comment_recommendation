def main():
    N, Q = map(int, input().split())
    edges = [[] for i in range(N+1)]
    for i in range(N-1):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    queries = []
    for i in range(Q):
        c, d = map(int, input().split())
        queries.append((c, d))
    dists = [-1] * (N+1)
    dists[1] = 0
    stack = [1]
    while stack:
        node = stack.pop()
        for nei in edges[node]:
            if dists[nei] == -1:
                dists[nei] = dists[node] + 1
                stack.append(nei)
    for c, d in queries:
        if (dists[c] + dists[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")
