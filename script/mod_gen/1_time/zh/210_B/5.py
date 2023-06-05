def main():
    # 读入数据
    n = int(input())
    s = input()
    # 数据处理
    # 从前往后遍历，找到第一个1的位置
    for i in range(n):
        if s[i] == '1':
            # 判断是奇数还是偶数
            if i % 2 == 0:
                print('Takahashi')
            else:
                print('Aoki')
            break

if __name__ == '__main__':
    main()