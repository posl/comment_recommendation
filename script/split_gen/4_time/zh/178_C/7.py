def main():
    # 读取输入
    n = int(input())
    # 初始化
    a = [0] * n
    a[0] = 1
    a[1] = 2
    # 计算
    for i in range(2, n):
        a[i] = (a[i - 1] + a[i - 2]) % (10**9 + 7)
    # 输出
    print(a[n - 1])
