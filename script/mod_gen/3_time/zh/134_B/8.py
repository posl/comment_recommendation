def main():
    # 读取数据
    n, d = map(int, input().split())
    # 计算结果
    print((n + 2 * d) // (2 * d + 1))

if __name__ == '__main__':
    main()