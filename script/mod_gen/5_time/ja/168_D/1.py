def main():
    N, M = map(int, input().split())
    # 隣接リストを作成
    adj = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        adj[A].append(B)
        adj[B].append(A)
    # BFS
    from collections import deque
    dist = [-1] * N
    dist[0] = 0
    q = deque()
    q.append(0)
    while q:
        v = q.popleft()
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    # 答えを復元
    ans = [0] * N
    for v in range(N):
        for nv in adj[v]:
            if dist[v] == dist[nv] + 1:
                ans[v] = nv + 1
                break
    print('Yes')
    for v in range(1, N):
        print(ans[v])

if __name__ == '__main__':
    main()