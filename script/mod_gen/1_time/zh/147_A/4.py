def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 判断
    if a + b + c >= 22:
        print('bust')
    else:
        print('win')

if __name__ == '__main__':
    main()