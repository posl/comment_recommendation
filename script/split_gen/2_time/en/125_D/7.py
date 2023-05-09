def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(abs(A[0] - A[1]))
        return
    # 1. 全ての要素の和の絶対値を求める
    sum_abs = 0
    for a in A:
        sum_abs += abs(a)
    # 2. Aのうち、負の数の個数を求める
    cnt_minus = 0
    for a in A:
        if a < 0:
            cnt_minus += 1
    # 3. Aのうち、0の個数を求める
    cnt_zero = 0
    for a in A:
        if a == 0:
            cnt_zero += 1
    # 4. Aのうち、正の数の個数を求める
    cnt_plus = N - cnt_minus - cnt_zero
    # 5. Aのうち、負の数の個数が奇数個ならば、Aのうち、最も絶対値が小さい正の数を負の数とする
    if cnt_minus % 2 == 1:
        # 5-1. Aのうち、最も絶対値が小さい正の数を探す
        min_plus = 10 ** 9 + 1
        for a in A:
            if a > 0 and a < min_plus:
                min_plus = a
        # 5-2. Aのうち、最も絶対値が小さい正の数を負の数とする
        sum_abs -= 2 * min_plus
    # 6. 答えを出力する
    print(sum_abs)
