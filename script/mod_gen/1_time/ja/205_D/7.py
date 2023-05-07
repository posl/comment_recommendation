def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    # aの最大値を求める
    a_max = max(a)
    # aの最大値を超える最小の2のべき乗
    a_max_p2 = 1
    while a_max_p2 <= a_max:
        a_max_p2 *= 2
    # aの最大値を超える最小の2のべき乗の配列を作成
    a_max_p2_list = [1]
    while a_max_p2_list[-1] <= a_max:
        a_max_p2_list.append(a_max_p2_list[-1] * 2)
    # aの最大値を超える最小の2のべき乗の配列を逆順に並べる
    a_max_p2_list.reverse()
    # aの最大値を超える最小の2のべき乗の配列の要素数
    a_max_p2_list_len = len(a_max_p2_list)
    # aの最大値を超える最小の2のべき乗の配列の要素数を超える数値のリスト
    over_a_max_p2_list = []
    # aの最大値を超える最小の2のべき乗の配列の要素数を超える数値のリストの要素数
    over_a_max_p2_list_len = 0
    # aの最大値を超える最小の2のべき乗の配列の要素数を超える数値のリストの要素数を求める
    for i in range(a_max_p2_list_len):
        if a_max_p2_list[i] > n:
            over_a_max_p2_list_len = i
            break
    # aの最大値を超える最小の2のべき乗の配列の要素数を超える数値のリ

if __name__ == '__main__':
    main()