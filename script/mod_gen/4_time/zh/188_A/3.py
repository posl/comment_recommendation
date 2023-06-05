def main():
    # 读取输入
    x, y = map(int, input().split())
    # 处理
    if x < y:
        x, y = y, x
    # 输出
    if x - y < 3:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()