def main():
    # 读入数据
    # 读入一行数据，包含4个整数
    a, b, c, d = map(int, input().split())
    # 处理数据
    if a > c:
        print("Takahashi")

if __name__ == '__main__':
    main()