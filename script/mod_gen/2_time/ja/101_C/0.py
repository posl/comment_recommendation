def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # N, K = 8, 3
    # A = [7, 3, 1, 8, 4, 6, 2, 5]
    # print(N, K, A)
    # 1. 連続するK個の要素を選ぶ
    # 2. 選んだ要素それぞれの値を，選んだ要素の中の最小値で置き換える
    # 3. スヌケ君は，上の操作を何回か繰り返すことで，この数列の要素をすべて等しくしたいです．
    # 連続するK個の要素を選ぶ
    # 1. 連続するK個の要素の中の最小値を探す
    # 2. 連続するK個の要素の中の最小値で全ての要素を置き換える
    # 3. 1. 2. を繰り返す
    # 連続するK個の要素の中の最小値を探す
    # 1. 連続するK個の要素を選び、その最小値を探す
    # 2. 1. を繰り返す
    # 連続するK個の要素を選び、その最小値を探す
    # 1. K個の要素を選ぶ
    # 2. 1. を繰り返す
    # K個の要素を選ぶ
    # 1. Aの先頭からK個の要素を取り出す
    # 2. 取り出した要素の中の最小値を探す
    # 3. 1.

if __name__ == '__main__':
    main()