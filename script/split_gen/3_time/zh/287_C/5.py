def main():
    # 读取输入
    n, m = map(int, input().split())
    # 邻接表
    adj = [[] for _ in range(n)]
    # 读取边
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    # 判断
    for i in range(n):
        if len(adj[i]) > 2:
            print('No')
            return
    print('Yes')
    return
