def main():
    # 读入数据
    n, x, t = map(int, input().split())
    # 计算结果
    if n % x == 0:
        result = int(n / x) * t
    else:
        result = (int(n / x) + 1) * t
    # 输出结果
    print(result)

if __name__ == '__main__':
    main()