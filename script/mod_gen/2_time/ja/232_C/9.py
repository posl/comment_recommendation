def main():
    n, m = map(int, input().split())
    # m = 0のときは、全てのボールが繋がっていることになるのでYes
    if m == 0:
        print("Yes")
        return
    # a, b, c, dについて、i本目のひもがボールa[i]とボールb[i]を結ぶ、ボールc[i]とボールd[i]を結ぶという情報を格納する
    a = []
    b = []
    c = []
    d = []
    for _ in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for _ in range(m):
        c_i, d_i = map(int, input().split())
        c.append(c_i)
        d.append(d_i)
    # ボール1から順番に、ボール1, 2, 3, ..., nを並べ替えたものを考える
    # このとき、ボール1, 2, 3, ..., nを並べ替えたものをPとする
    # 2人のおもちゃが同じ形かどうかは、Pを固定して、a, b, c, dを全て調べることで判定できる
    # つまり、Pを固定して、a, b, c, dを全て調べることで、2人のおもちゃが同じ形かどうかを判定できる
    # このとき、a, b, c, dのうち、ボール1, 2, 3, ..., nを結ぶひもがあるかどうかを調べることで、Pを固定して、a, b, c, dを全て調べることができる
    # このとき、ボール1, 2

if __name__ == '__main__':
    main()