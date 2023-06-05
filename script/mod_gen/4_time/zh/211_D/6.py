def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        adj[a].append(b)
        adj[b].append(a)
    d = [float('inf')] * N
    d[0] = 0
    q = [0]
    while q:
        qq = []
        for p in q:
            for r in adj[p]:
                if d[r] > d[p] + 1:
                    d[r] = d[p] + 1
                    qq.append(r)
        q = qq
    print(d[N - 1] if d[N - 1] != float('inf') else 0)
main()
