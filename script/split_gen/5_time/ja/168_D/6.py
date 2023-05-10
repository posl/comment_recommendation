def main():
    N, M = map(int, input().split())
    AB = [map(int, input().split()) for _ in range(M)]
    A, B = [list(i) for i in zip(*AB)]
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for a, b in zip(A, B):
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # BFS
    from collections import deque
    q = deque([0])
    ans = [None] * N
    ans[0] = 0
    while q:
        v = q.popleft()
        for u in adj[v]:
            if ans[u] is None:
                ans[u] = v + 1
                q.append(u)
    print('Yes')
    for a in ans[1:]:
        print(a)
