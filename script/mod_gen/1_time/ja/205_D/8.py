def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    # 1を除く、aの要素を2乗したものをリストに格納
    b = [i**2 for i in a if i != 1]
    # aの要素を2乗したものの最大値を求める
    max_b = max(b)
    # aの要素の最大値を求める
    max_a = max(a)
    # 1を除く、aの要素を2乗したものの最大値を求める
    max_b = max(b)
    # aの要素の最大値より小さい、1を除く、aの要素を2乗したものをリストに格納
    c = [i for i in b if i < max_a]
    # aの要素の最大値より小さい、1を除く、aの要素を2乗したものの最大値を求める
    max_c = max(c)
    # aの要素の最大値より小さい、1を除く、aの要素を2乗したものの最大値より小さい、1を除く、aの要素を2乗したものをリストに格納
    d = [i for i in c if i < max_b]
    # aの要素の最大値より小さい、1を除く、aの要素を2乗したものの最大値より小さい、1を除く、aの要素を2乗したものの最大値を求める
    max_d = max(d)
    # aの要素の最大値より小さい、1を除く、aの要素を2乗したものの最大値より小さい、1を除く、aの要素を2乗したものの最大値より小さい、1

if __name__ == '__main__':
    main()