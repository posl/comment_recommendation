def main():
    N, M = map(int, input().split())
    M = M ** (1 / 2)
    M = int(M)
    if M == 0:
        print(-1)
        return
    else:
        # 棋盘
        chess = [[0 for _ in range(N)] for _ in range(N)]
        # 起始位置
        chess[0][0] = 1
        # 从起始位置开始搜索
        search(chess, 0, 0, 1, M)
        # 打印结果
        for i in range(N):
            print(*chess[i])
