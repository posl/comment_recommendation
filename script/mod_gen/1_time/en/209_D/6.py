def solve():
    N, Q = map(int, input().split())
    path = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        path[a-1].append(b-1)
        path[b-1].append(a-1)
    query = [list(map(int, input().split())) for _ in range(Q)]
    dist = [0]*N
    q = [0]
    while q:
        v = q.pop()
        for nv in path[v]:
            if dist[nv] == 0:
                dist[nv] = dist[v] + 1
                q.append(nv)
    for c, d in query:
        if (dist[c-1] + dist[d-1]) % 2 == 0:
            print("Town")
        else:
            print("Road")
solve()

if __name__ == '__main__':
    solve()