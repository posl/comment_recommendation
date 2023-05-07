def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for i in range(Q)]
    # ある数を全てXにするために必要な操作回数は、
    # その数にXを足した数の桁数を足したもの
    # 例えば、A_i = 1234, X_i = 5678のとき、
    # 1234 + 5678 = 6912
    # 6912は4桁なので、1234に5678を足すのに必要な操作回数は4
    # これをすべてのA_iについて計算すると、
    # 1234 + 5678 = 6912
    # 3141 + 5678 = 8819
    # 2718 + 5678 = 8396
    # 1414 + 5678 = 7092
    # 1618 + 5678 = 7296
    # 0 + 5678 = 5678
    # 7777 + 5678 = 13455
    # 2552 + 5678 = 8230
    # 5368 + 5678 = 11046
    # 9982 + 5678 = 15660
    # となる。
    # これを桁数を求めるための関数を作成し、
    # それぞれのA_iに対して、A_i + X_iを計算し、
    # 桁数を求める関数に入れることで、
    # そのA_iに対してX_iを足すのに必要な操作回数を求めることができる。
    # この操作をすべてのA_iに対して行うと、
    # 6912 + 8819 + 8396 + 7092 + 7296 + 5678 + 13455 +

if __name__ == '__main__':
    main()