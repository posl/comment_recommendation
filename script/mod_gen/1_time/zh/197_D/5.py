def main():
    # 输入
    N = int(input())
    x0, y0 = map(float, input().split())
    x2, y2 = map(float, input().split())
    # 计算
    x1 = (x0 + x2 + (y2 - y0) * (3 ** 0.5)) / 2
    y1 = (y0 + y2 - (x2 - x0) * (3 ** 0.5)) / 2
    # 输出
    print(x1, y1)

if __name__ == '__main__':
    main()