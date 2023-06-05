def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 逻辑处理
    if a**2 + b**2 < c**2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()