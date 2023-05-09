def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 始点となる1以外の部屋について、
    # 1にたどり着くために必要な最短経路をBFSで求める
    # その際の各部屋の親を記録しておく
    # そして、親の部屋番号を出力すればよい
    from collections import deque
    adj = [[] for _ in range(N+1)]
    for i in range(M):
        adj[A[i]].append(B[i])
        adj[B[i]].append(A[i])
    q = deque()
    q.append(1)
    parent = [-1] * (N+1)
    parent[1] = 0
    while q:
        v = q.popleft()
        for nv in adj[v]:
            if parent[nv] == -1:
                parent[nv] = v
                q.append(nv)
    if -1 in parent[2:]:
        print("No")
    else:
        print("Yes")
        for i in range(2, N+1):
            print(parent[i])

if __name__ == '__main__':
    main()