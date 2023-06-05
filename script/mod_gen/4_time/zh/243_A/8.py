def main():
    # 读取输入
    v, a, b, c = map(int, input().split())
    # 模拟
    while True:
        # 高桥的父亲
        v -= a
        if v < 0:
            print('F')
            break
        # 高桥的母亲
        v -= b
        if v < 0:
            print('M')
            break
        # 高桥
        v -= c
        if v < 0:
            print('T')
            break

if __name__ == '__main__':
    main()