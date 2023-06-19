def main():
    #读取输入
    r, c = map(int, input().split())
    #处理
    #判断是不是偶数行偶数列
    if r % 2 == 0 and c % 2 == 0:
        print('黑色')
    elif r % 2 != 0 and c % 2 != 0:
        print('黑色')
    else:
        print('白色')

if __name__ == '__main__':
    main()