def main():
    # 读取输入
    n = int(input())
    # 依次尝试买 0，1，2，…，n/7 个甜甜圈
    for i in range(n // 7 + 1):
        # 甜甜圈的总价
        price = 7 * i
        # 剩余的钱
        rest = n - price
        # 如果剩余的钱可以被 4 整除，说明可以买到蛋糕
        if rest % 4 == 0:
            print('Yes')
            return
    # 以上循环结束后，没有找到可以买到甜甜圈和蛋糕的方案
    print('No')

if __name__ == '__main__':
    main()