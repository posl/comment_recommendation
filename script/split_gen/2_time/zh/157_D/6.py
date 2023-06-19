def main():
    # 读取输入
    N, M, K = map(int, input().split())
    # 读取友谊关系
    friends = [tuple(map(int, input().split())) for i in range(M)]
    # 读取阻隔关系
    blocks = [tuple(map(int, input().split())) for i in range(K)]
    # 生成邻接表
    adj = [[] for i in range(N)]
    for f in friends:
        adj[f[0]-1].append(f[1]-1)
        adj[f[1]-1].append(f[0]-1)
    # 生成距离表
    dist = [[-1 for i in range(N)] for j in range(N)]
    for i in range(N):
        dist[i][i] = 0
        queue = [i]
        while len(queue) > 0:
            v = queue.pop(0)
            for u in adj[v]:
                if dist[i][u] < 0:
                    dist[i][u] = dist[i][v] + 1
                    queue.append(u)
    # 计算结果
    result = [0 for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if dist[i][j] < 0:
                continue
            if dist[i][j] == 1:
                continue
            for b in blocks:
                if b[0] == i+1 and b[1] == j+1:
                    break
                if b[0] == j+1 and b[1] == i+1:
                    break
            else:
                result[i] += 1
    # 输出结果
    print(" ".join(map(str, result)))
