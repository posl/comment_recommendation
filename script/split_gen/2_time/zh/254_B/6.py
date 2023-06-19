def main():
    # 读取输入
    n = int(input())
    # 初始化
    a = [[0 for j in range(n)] for i in range(n)]
    # 迭代
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                a[i][j] = 1
            else:
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    # 输出
    for i in range(n):
        for j in range(i + 1):
            print(a[i][j], end=" ")
        print()
