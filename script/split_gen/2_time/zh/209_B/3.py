def main():
    # 读取输入
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # 计算
    sum = 0
    for i in range(n):
        if i % 2 == 1:
            sum += a[i] - 1
        else:
            sum += a[i]
    # 输出
    if sum <= x:
        print("Yes")
    else:
        print("No")
