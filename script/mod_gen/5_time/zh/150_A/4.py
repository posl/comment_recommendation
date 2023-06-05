def main():
    # 读取输入
    K, X = map(int, input().split())
    # 解决问题
    if K * 500 >= X:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()