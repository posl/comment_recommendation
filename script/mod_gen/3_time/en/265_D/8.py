def main():
    N, P, Q, R = list(map(int, input().split()))
    A = list(map(int, input().split()))
    # 1. 全ての条件を満たす x, y, z, w の組み合わせを列挙する
    # 2. それぞれの組み合わせについて、条件を満たすかどうか判定する
    # 3. どれか一つでも条件を満たす組み合わせがあれば Yes を出力する
    # 4. どれも条件を満たさない組み合わせがあれば No を出力する
    # 1. 全ての条件を満たす x, y, z, w の組み合わせを列挙する
    # x, y, z, w が全て異なる組み合わせを列挙する
    # x, y, z, w が全て異なる組み合わせは、x, y, z, w の組み合わせの数の約数の組み合わせとなる
    # 例えば、x, y, z, w の組み合わせの数が 8 であれば、
    #   (x, y, z, w) = (0, 1, 2, 3)
    #   (x, y, z, w) = (0, 1, 2, 4)
    #   (x, y, z, w) = (0, 1, 2, 5)
    #   (x, y, z, w) = (0, 1, 2, 6)
    #   (x, y, z, w) = (0, 1, 2, 7)
    #   (x, y, z, w) = (0, 1, 3, 4)
    #   (x, y, z, w) = (0, 1, 3, 5)
    #

if __name__ == '__main__':
    main()