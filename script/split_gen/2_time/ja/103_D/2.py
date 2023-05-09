def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    E = [[] for _ in range(N)]
    for i in range(M):
        E[A[i]].append(B[i])
        E[B[i]].append(A[i])
    #print(E)
    #print(A)
    #print(B)
    #print(N, M)
    # 深さ優先探索
    def dfs(v):
        #print("v", v)
        #print("visited", visited)
        #print("group", group)
        visited[v] = True
        group[v] = g
        for u in E[v]:
            if not visited[u]:
                dfs(u)
    # 連結成分分解
    visited = [False] * N
    group = [-1] * N
    g = 0
    for v in range(N):
        if not visited[v]:
            dfs(v)
            g += 1
    #print("visited", visited)
    #print("group", group)
    #print("g", g)
    # 連結成分の頂点数
    count = [0] * g
    for i in range(N):
        count[group[i]] += 1
    #print("count", count)
    # 連結成分の橋数
    bridge = [0] * g
    for i in range(M):
        if group[A[i]] != group[B[i]]:
            bridge[group[A[i]]] += 1
            bridge[group[B[i]]] += 1
    #print("bridge", bridge)
    # 連結成分の橋数が 0 の数
    zero = 0
    for i in range(g):
        if bridge[i] == 0:
            zero += 1
    #print("zero", zero)
    # 答え
    ans = max(0, zero - 1)
    print(ans)
