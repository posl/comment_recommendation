def count_chess():
    # 读取输入
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    # 计算棋子数
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    # 输出结果
    print(count)
