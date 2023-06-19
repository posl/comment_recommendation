def main():
    # 读取输入
    x = int(input())
    # 确定是否可以用x个100日元的硬币凑出x日元
    if x % 100 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()