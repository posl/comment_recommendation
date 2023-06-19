def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 从B瓶中移动到A瓶中
    B = B + C
    # 从A瓶中移动到B瓶中
    C = B - A
    # 从B瓶中移动到A瓶中
    B = B - C
    # 输出结果
    print(C)

if __name__ == '__main__':
    main()