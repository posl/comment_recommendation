def main():
    # 读取输入
    v, a, b, c = map(int, input().split())
    # 依次计算
    while v > 0:
        if v >= a:
            v -= a
        else:
            print('F')
            return
        if v >= b:
            v -= b
        else:
            print('M')
            return
        if v >= c:
            v -= c
        else:
            print('T')
            return

if __name__ == '__main__':
    main()