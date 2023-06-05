def solve():
    # 入力
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 0の数
    num_zero = a.count(0)
    # 0の数だけ0の組み合わせがある
    if num_zero > 0:
        k -= num_zero * (n - num_zero)
        # 0がk番目に来る場合
        if k <= 0:
            print(0)
            return
    # 0を除いた数値に変換
    a = [x for x in a if x != 0]
    # 昇順に並べる
    a.sort(key=abs)
    # 負の数の数
    num_minus = len([x for x in a if x < 0])
    # 負の数の数が奇数の場合
    if num_minus % 2 == 1:
        # 0がk番目に来る場合
        if k <= 0:
            print(0)
            return
        # 負の数をk番目に来るように調整
        a = a[1:]
        k -= 1
    # 0を除いた数値の数
    n = len(a)
    # 0を除いた数値の数の組み合わせの数
    num_comb = n * (n - 1) // 2
    # kが大きすぎる場合
    if k > num_comb:
        print(0)
        return
    # k番目の数値を出力
    print(a[k - 1])
solve()
