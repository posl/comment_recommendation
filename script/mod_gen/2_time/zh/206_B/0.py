def main():
    # 读入数据
    n = int(input())
    # 处理数据
    price = int(1.08 * n)
    # 输出结果
    if price < 206:
        print('Yay!')
    elif price == 206:
        print('so-so')
    else:
        print(':(')

if __name__ == '__main__':
    main()