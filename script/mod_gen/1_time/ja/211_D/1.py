def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        G[A].append(B)
        G[B].append(A)
    # BFS
    from collections import deque
    dist = [-1] * N
    dist[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
    if dist[N-1] == -1:
        print(0)
        return
    # 最短経路の数を数える
    ans = 0
    que = deque([N-1])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] != dist[v] - 1:
                continue
            ans += 1
            que.append(nv)
    print(ans % (10**9+7))

if __name__ == '__main__':
    main()