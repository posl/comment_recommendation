def main():
    N = int(input())
    G = [[] for _ in range(10)]
    for _ in range(N):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    P = list(map(int, input().split()))
    for i in range(1, 10):
        G[i].sort()
    ans = 10**10
    for i in range(8):
        for j in range(i+1, 8):
            for k in range(j+1, 8):
                for l in range(k+1, 8):
                    for m in range(l+1, 8):
                        for n in range(m+1, 8):
                            for o in range(n+1, 8):
                                for p in range(o+1, 8):
                                    Q = [P[i], P[j], P[k], P[l], P[m], P[n], P[o], P[p]]
                                    if check(G, Q):
                                        ans = min(ans, bfs(G, Q))
    if ans == 10**10:
        print(-1)
    else:
        print(ans)
