def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 隣接リストを隣接行列に変換
    # adj_mat = [[0] * N for _ in range(N)]
    # for i in range(N):
    #     for j in adj[i]:
    #         adj_mat[i][j] = 1
    #         adj_mat[j][i] = 1
    # print(adj_mat)
    # 始点
    start = 0
    # 終点
    goal = N-1
    # 経路数
    paths = 0
    # 深さ優先探索
    stack = [start]
    while stack:
        cur = stack.pop()
        if cur == goal:
            paths += 1
            continue
        for i in adj[cur]:
            if i in stack:
                continue
            stack.append(i)
    print(paths % (10**9+7))
