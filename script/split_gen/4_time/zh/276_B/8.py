def main():
    # 读入数据
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    # 建立邻接表
    adj = [[] for _ in range(n)]
    for i in range(m):
        adj[a[i] - 1].append(b[i] - 1)
        adj[b[i] - 1].append(a[i] - 1)
    # 打印结果
    for i in range(n):
        print(len(adj[i]), end=" ")
        for j in range(len(adj[i])):
            print(adj[i][j] + 1, end=" ")
        print()
