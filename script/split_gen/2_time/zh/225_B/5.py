def solve(n, a, b):
    # 1. 根据边的信息，建立邻接表
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        adj[a[i]].append(b[i])
        adj[b[i]].append(a[i])
    # 2. 找到度数为n-1的节点
    for i in range(1, n + 1):
        if len(adj[i]) == n - 1:
            return 'Yes'
    return 'No'
