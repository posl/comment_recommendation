def main():
    # 读入数据
    a, n = map(int, input().split())
    # 初始化
    count = 0
    # 用循环来实现
    while n > 1:
        if n % a == 0:
            n //= a
        else:
            n -= 1
        count += 1
    print(count)
