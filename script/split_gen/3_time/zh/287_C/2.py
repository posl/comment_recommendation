def main():
    # 读入数据
    n, m = map(int, input().split())
    # 生成邻接表
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    # 判断是否为路径图
    for u in range(n):
        if len(adj[u]) > 2:
            print("No")
            return
    print("Yes")
    return
