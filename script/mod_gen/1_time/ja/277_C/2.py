def main():
    N = int(input())
    H = []
    for _ in range(N):
        A, B = map(int, input().split())
        H.append(A)
        H.append(B)
    H = list(set(H))
    H.sort()
    H = {h:i for i, h in enumerate(H)}
    G = [[] for _ in range(len(H))]
    for _ in range(N):
        A, B = map(int, input().split())
        G[H[A]].append(H[B])
        G[H[B]].append(H[A])
    INF = 10**18
    dist = [INF] * len(H)
    dist[0] = 0
    que = [0]
    while que:
        v = que.pop()
        for nv in G[v]:
            if dist[nv] == INF:
                dist[nv] = dist[v] + 1
                que.append(nv)
    print(max(dist))

if __name__ == '__main__':
    main()