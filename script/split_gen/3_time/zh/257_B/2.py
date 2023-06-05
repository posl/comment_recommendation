def main():
    # 读入问题数据
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    # 生成棋子的位置列表
    chess = [0] * n
    for i in range(k):
        chess[a[i] - 1] = 1
    # 执行Q次操作
    for i in range(q):
        # 棋子移动
        if chess[l[i] - 1] == 1:
            for j in range(n):
                if chess[j] == 0:
                    chess[j] = 1
                    chess[l[i] - 1] = 0
                    break
    # 打印结果
    for i in range(n):
        if chess[i] == 1:
            print(i + 1, end=" ")
    print()
