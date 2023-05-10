Synthesizing 10/10 solutions

=======
Suggestion 1

def check(h, w):
    for i in range(3):
        if sum(h[i]) != h[i][0] * 3:
            return False
    for i in range(3):
        if sum(w[i]) != w[i][0] * 3:
            return False
    return True

=======
Suggestion 2

def solve(h1,h2,h3,w1,w2,w3):
    if h1+h2+h3 != w1+w2+w3:
        return 0
    return 1

=======
Suggestion 3

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    # print(h1, h2, h3, w1, w2, w3)
    # print((h1, h2, h3), (w1, w2, w3))
    # print((h1, h2, h3) == (w1, w2, w3))
    # print((h1, h2, h3) != (w1, w2, w3))
    # print((h1, h2, h3) < (w1, w2, w3))
    # print((h1, h2, h3) > (w1, w2, w3))
    # print((h1, h2, h3) <= (w1, w2, w3))
    # print((h1, h2, h3) >= (w1, w2, w3))
    # print((h1, h2, h3) + (w1, w2, w3))
    # print((h1, h2, h3) - (w1, w2, w3))
    # print((h1, h2, h3) * (w1, w2, w3))
    # print((h1, h2, h3) / (w1, w2, w3))
    # print((h1, h2, h3) // (w1, w2, w3))
    # print((h1, h2, h3) % (w1, w2, w3))
    # print((h1, h2, h3) ** (w1, w2, w3))
    # print((h1, h2, h3) & (w1, w2, w3))
    # print((h1, h2, h3) | (w1, w2, w3))
    # print((h1, h2, h3) ^ (w1, w2, w3))
    # print((h1, h2, h3) << (w1, w2, w3))
    # print((h1, h2, h3) >> (w1, w2

=======
Suggestion 4

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print((h1+h2+h3)*(w1+w2+w3)//(h1*h2*h3+w1*w2*w3))

=======
Suggestion 5

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    # x1, x2, x3, x4, x5, x6, x7, x8, x9 = map(int, input().split())
    # h = [h1, h2, h3]
    # w = [w1, w2, w3]
    # x = [x1, x2, x3, x4, x5, x6, x7, x8, x9]

    # 重複組合せ
    # https://qiita.com/derodero24/items/91b6468e66923a87f39f
    # https://qiita.com/derodero24/items/91b6468e66923a87f39f
    # https://qiita.com/derodero24/items/91b6468e66923a87f39f

    # 重複組合せ
    # https://qiita.com/gogotealove/items/11f9e83218926211083a
    # https://qiita.com/gogotealove/items/11f9e83218926211083a
    # https://qiita.com/gogotealove/items/11f9e83218926211083a

    # 重複組合せ
    # https://qiita.com/gogotealove/items/11f9e83218926211083a
    # https://qiita.com/gogotealove/items/11f9e83218926211083a
    # https://qiita.com/gogotealove/items/11f9e83218926211083a

    # 重複組合せ
    # https://qiita.com/gogotealove/items/11f9e83218926211083a
    # https://qiita.com/gogotealove/items/11f9e83218926211083a
    # https://qiita.com/gogotealove/items/11f9e83218926211083a

    # 重複組合せ
    # https://qiita.com/gogote

=======
Suggestion 6

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    count = 0
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                if i + j == h1 and j + k == h2 and i + k == h3 and i + j + k == w1 and i + j + k == w2 and i + j + k == w3:
                    count += 1
    print(count)

=======
Suggestion 7

def my_print(l):
    for i in range(3):
        print(l[i][0], l[i][1], l[i][2])

=======
Suggestion 8

def p256():
    # 入力
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    # 出力
    print(0)

=======
Suggestion 9

def solve(h1, h2, h3, w1, w2, w3):
    # ここに書き込む
    return 0

=======
Suggestion 10

def f(h1, h2, h3, w1, w2, w3):
    # 3x3のマス目に、以下の条件をすべて満たすように各マスに正の整数を1つずつ書きこむことを考えます。
    # i=1,2,3について、上からi行目に書きこんだ数の和がhiになる。
    # j=1,2,3について、左からj列目に書きこんだ数の和がwjになる。
    # 例えば(h1, h2, h3) = (5, 13, 10), (w1, w2, w3) = (6, 13, 9)のとき、以下の3通りの書きこみ方はすべて条件を満たしています。
    # さて、条件を満たす書きこみ方は全部で何通り存在しますか？
    # 制約
    # 3 ≦ h1, h2, h3, w1, w2, w3 ≦ 30
    # 入力される値はすべて整数
    # 入力
    # 入力は以下の形式で標準入力から与えられる。
    # h1 h2 h3 w1 w2 w3
    # 出力
    # 条件を満たす書きこみ方が何通りあるかを出力せよ。
    # 入力例1
    # 3 4 6 3 3 7
    # 出力例1
    # 1
    # 条件を満たす数の書きこみ方は次の1通りのみです。よって1を出力します。
    # 入力例2
    # 3 4 5 6 7 8
    # 出力例2
    # 0
    # 条件を満たす書きこみ
