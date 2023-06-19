def problem256_b():
    # 读取输入
    N = int(input())
    A = [int(x) for x in input().split()]
    # 棋子位置
    chess = [0 for _ in range(4)]
    # 移除棋子数量
    P = 0
    # 操作
    for i in range(N):
        # 在0号方格放一个棋子
        chess[0] += 1
        # 将每个棋子在方格上向前推进A[i]个方格
        for j in range(4):
            if chess[j] > 0:
                if j + A[i] < 4:
                    chess[j + A[i]] += chess[j]
                P += chess[j]
                chess[j] = 0
    print(P)
