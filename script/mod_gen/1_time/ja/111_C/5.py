def main():
    # 入力
    n = int(input())
    v = list(map(int, input().split()))
    # 偶数番目と奇数番目に分ける
    v_odd = v[0::2]
    v_even = v[1::2]
    # それぞれの数の個数をカウント
    from collections import Counter
    c_odd = Counter(v_odd)
    c_even = Counter(v_even)
    # それぞれの最も多い数を求める
    max_odd = c_odd.most_common()[0][0]
    max_even = c_even.most_common()[0][0]
    # 最も多い数が同じ場合
    if max_odd == max_even:
        # それぞれの最も多い数以外の数の個数を求める
        max_odd_count = c_odd.most_common()[0][1]
        max_even_count = c_even.most_common()[0][1]
        max_odd_count2 = c_odd.most_common()[1][1]
        max_even_count2 = c_even.most_common()[1][1]
        # それぞれの最も多い数以外の数の個数の和が答え
        print(n - max_odd_count - max_even_count2)
    # 最も多い数が異なる場合
    else:
        # それぞれの最も多い数の個数を求める
        max_odd_count = c_odd.most_common()[0][1]
        max_even_count = c_even.most_common()[0][1]
        # それぞれの最も多い数の個数の和が答え
        print(n - max_odd_count - max_even_count)

if __name__ == '__main__':
    main()