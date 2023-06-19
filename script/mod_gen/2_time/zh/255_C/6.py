def main():
    # 读取输入
    x, a, d, n = map(int, input().split())
    # 从x中减去a，得到x的偏移量
    x -= a
    # 如果x是d的倍数
    if x % d == 0:
        # 计算x的偏移量与d的商
        x //= d
        # 如果x是正数且n大于等于x
        if x >= 0 and n >= x:
            # 输出n-x
            print(n - x)
            # 退出程序
            exit()
        # 如果x是负数且n小于等于x
        elif x < 0 and n <= x:
            # 输出n-x
            print(n - x)
            # 退出程序
            exit()
    # 否则，输出n
    print(n)

if __name__ == '__main__':
    main()