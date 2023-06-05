def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 初始化
    P = 0
    # 4个方块
    squares = [0] * 4
    # 模拟
    for i in range(N):
        # 在0号方块放置一个棋子
        squares[0] += 1
        # 移动棋子
        for j in range(4):
            # 移动
            squares[j] += A[i]
            # 如果目标方块不存在
            if squares[j] >= 4:
                # 移除棋子
                squares[j] = 0
                # P加1
                P += 1
    # 输出
    print(P)

if __name__ == '__main__':
    main()