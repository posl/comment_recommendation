def main():
    # 读取输入
    a = list(map(int, input().split()))
    # 排序
    a.sort()
    # 判断是否为等差数列
    if a[1] - a[0] == a[2] - a[1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()