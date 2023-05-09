def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    # Aの最大値を求める
    max_A = max(A)
    # Aの最大値を超える最小の2のべき乗を求める
    # 例：max_A = 8の場合、2**3 = 8
    # 例：max_A = 9の場合、2**4 = 16
    max_pow = 1
    while max_pow <= max_A:
        max_pow *= 2
    # 2のべき乗の数列を求める
    # 例：max_pow = 8の場合、[1, 2, 4, 8]
    pow_list = [1]
    for _ in range(N):
        pow_list.append(pow_list[-1] * 2)
    # Aの要素を2のべき乗の数列の要素に変換する
    # 例：A = [3, 5, 6, 7]の場合、[2, 4, 8, 9]
    A = [pow_list.index(a) for a in A]
    # 2のべき乗の数列の累積和を求める
    # 例：pow_list = [1, 2, 4, 8]の場合、[1, 3, 7, 15]
    pow_list_sum = [0]
    for pow in pow_list:
        pow_list_sum.append(pow_list_sum[-1] + pow)
    # Aの要素を2のべき乗の数列の要素に変換したものの累積和を求める
    # 例：A = [2, 4, 8, 9]の場合、[0, 2, 6, 14, 23]
    A_sum = [0]
    for a in A:
        A_sum.append(A_sum[-1] + a)
    # クエリ毎に2のべ

if __name__ == '__main__':
    main()