def main():
    # 读取输入
    x, y, z = map(int, input().split())
    # 交换
    x, y = y, x
    x, z = z, x
    # 输出
    print(x, y, z)

if __name__ == '__main__':
    main()