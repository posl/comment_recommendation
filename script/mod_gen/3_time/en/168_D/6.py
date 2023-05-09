def solve():
    N, M = [int(x) for x in input().split()]
    A = []
    B = []
    for i in range(M):
        a, b = [int(x) for x in input().split()]
        A.append(a)
        B.append(b)
    # 0-indexed
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    # 0-indexed
    graph = [[] for i in range(N)]
    for i in range(M):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])
    # 0-indexed
    visited = [False] * N
    # 0-indexed
    parent = [-1] * N
    # 0-indexed
    depth = [-1] * N
    # 0-indexed
    queue = [0]
    visited[0] = True
    depth[0] = 0
    while queue:
        q = queue.pop()
        for n in graph[q]:
            if not visited[n]:
                visited[n] = True
                parent[n] = q
                depth[n] = depth[q] + 1
                queue.append(n)
    # 0-indexed
    signpost = [-1] * N
    for i in range(N):
        if i == 0:
            continue
        signpost[i] = parent[i]
    print("Yes")
    for i in range(N):
        if i == 0:
            continue
        print(signpost[i] + 1)
solve()

if __name__ == '__main__':
    solve()