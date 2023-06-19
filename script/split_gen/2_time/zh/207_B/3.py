def main():
    a, b, c, d = map(int, input().split())
    if a >= b * d:
        print(-1)
        return
    # 一次操作后红球的数量
    red = a
    # 一次操作后蓝球的数量
    blue = 0
    # 操作的次数
    count = 0
    while True:
        # 如果蓝球的数量大于红球的数量的d倍
        if blue > red * d:
            print(count)
            return
        # 否则，继续操作
        red += c
        blue += b
        count += 1
