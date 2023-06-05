def main():
    # 读入数据
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    # 建立邻接表
    adj = [[] for _ in range(N)]
    for a, b in AB:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 建立阻隔表
    block = [[False]*N for _ in range(N)]
    for c, d in CD:
        block[c-1][d-1] = True
        block[d-1][c-1] = True
    # 计算候选人数
    for i in range(N):
        ans = 0
        for j in range(N):
            if i == j:
                continue
            if j in adj[i]:
                continue
            if block[i][j]:
                continue
            # 到这里说明j是i的候选人
            # 遍历从i到j的所有路径
            # 为了避免重复，规定只能往后走
            # 用栈实现dfs
            stack = [i]
            while stack:
                # 取出栈顶元素
                now = stack.pop()
                # 如果已经到达j，则计数+1
                if now == j:
                    ans += 1
                    break
                # 如果没到达，则将邻接点入栈
                for k in adj[now]:
                    if k in stack:
                        continue
                    stack.append(k)
        print(ans, end=' ')
    print()
