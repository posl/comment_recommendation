def main():
    # 读取输入
    a, b = map(int, input().split())
    # 判断条件
    if (a == 4 and b == 5) or (a == 1 and b == 3) or (a == 1 and b == 5) or (a == 3 and b == 4) or (a == 1 and b == 4) or (a == 3 and b == 5):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()