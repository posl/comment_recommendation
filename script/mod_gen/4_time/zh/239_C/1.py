def main():
    # 读取输入
    x1, y1, x2, y2 = map(int, input().split())
    # 两点距离
    dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    # 判断是否为整数
    if dist.is_integer():
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()