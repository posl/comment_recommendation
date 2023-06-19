def main():
    # 读取输入
    a, b, c, d = map(int, input().split())
    # 判断是否可以实现
    if a < b * d:
        print(-1)
        return
    # 计算所需最少操作数
    # 操作次数
    cnt = 0
    # 红色球数量
    red = 0
    # 蓝色球数量
    blue = a
    # 蓝色球数量大于红色球数量的d倍时，停止操作
    while blue > red * d:
        # 操作次数加1
        cnt += 1
        # 蓝色球数量增加b个
        blue += b
        # 红色球数量增加c个
        red += c
    # 打印结果
    print(cnt)

if __name__ == '__main__':
    main()