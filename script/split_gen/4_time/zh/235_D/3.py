def main():
    # 读取输入
    a, n = map(int, input().split())
    # 从1开始，尝试将1变为n
    x = 1
    # 记录操作次数
    count = 0
    # 当x小于n时，循环
    while x < n:
        # 将x乘以a
        x *= a
        # 记录操作次数
        count += 1
    # 如果x等于n，打印count
    if x == n:
        print(count)
    # 如果x大于n，打印-1
    else:
        print(-1)
