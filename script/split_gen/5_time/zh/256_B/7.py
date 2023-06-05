def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    # 初始化
    p = 0
    # 循环
    for i in range(n):
        # 1. 在0号方格放一个棋子，现在0号方格有一个棋子。
        # 2. 将方格上的每个棋子向前推进1个方格。经过这些操作，广场1有一个棋子。
        p += a[i] - 1
    # 输出结果
    print(p)
