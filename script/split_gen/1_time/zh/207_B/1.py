def main():
    # 读取数据
    a, b, c, d = map(int, input().split())
    # 循环
    count = 0
    while a > c * d:
        a += b
        c += d
        count += 1
    # 判断
    if a <= c * d:
        print(count)
    else:
        print(-1)
