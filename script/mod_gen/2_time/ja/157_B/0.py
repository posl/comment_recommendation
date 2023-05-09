def main():
    # A_{1, 1} A_{1, 2} A_{1, 3}
    # A_{2, 1} A_{2, 2} A_{2, 3}
    # A_{3, 1} A_{3, 2} A_{3, 3}
    A = [list(map(int, input().split())) for _ in range(3)]
    # N
    N = int(input())
    # b_1
    # .
    # .
    # .
    # b_N
    b = [int(input()) for _ in range(N)]
    # 1 ≦ N ≦ 10
    # 1 ≦ b_i ≦ 100
    # b_i ≠ b_j (i ≠ j)
    # 上記の制約より、
    # 1 ≦ N ≦ 10
    # 1 ≦ b_i ≦ 100
    # 1 ≦ b_j ≦ 100
    # i ≠ j
    # となる。
    # よって、bの要素数は最大100個である。
    # bの要素数は最大100個であるため、
    # bの要素数分のリストを作成し、
    # そのリストの要素を0に初期化する。
    bingo = [0] * 100
    # bの要素数分ループを回す。
    for i in range(N):
        # bの要素数分ループを回す。
        for j in range(N):
            # bのi番目の要素が、Aのj番目の要素と等しい場合
            if b[i] == A[j]:
                # bingoのj番目の要素に1を代入する。
                bingo[j] = 1
    # bingoの0番目の要素と1番目の要素、2番目の要素が全て1の場合、
    # bingoの3番目の要素と4番目の要素、5番目の要素が全て1の場合、
    # bingoの6番目の要素と

if __name__ == '__main__':
    main()