def solve():
    # 读入数据
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # 构造邻接表
    adj = [[] for _ in range(N+1)]
    for i in range(N-1):
        adj[a[i]].append(b[i])
        adj[b[i]].append(a[i])
    # 从顶点1开始深度优先遍历
    visited = [False] * (N+1)
    visited[1] = True
    stack = [1]
    while stack:
        v = stack.pop()
        for i in range(len(adj[v])):
            if not visited[adj[v][i]]:
                visited[adj[v][i]] = True
                stack.append(adj[v][i])
    # 判断是否所有顶点都被访问过
    for i in range(1, N+1):
        if not visited[i]:
            print('No')
            return
    print('Yes')
