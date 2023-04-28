Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    #print(h1, h2, h3, w1, w2, w3)
    # 1-9の数字を1つずつ入れる
    # 9!通り
    # 1-9の数字を1つずつ入れる
    # 9!通り
    # 1-9の数字を1つずつ入れる
    # 9!通り
    # 1-9の数字を1つずつ入れる
    # 9!通り
    # 1-9の数字を1つずつ入れる
    # 9!通り
    # 1-9の数字を1つずつ入れる
    # 9!通り
    # 1-9の数字を1つずつ入れる
    # 9!通り
    # 1-9の数字を1つずつ入れる
    # 9!通り
    # 1-9の数字を1��

=======
Suggestion 2

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print((h1 + h2 + h3) * (w1 + w2 + w3) - h1 * w1 - h2 * w2 - h3 * w3)

=======
Suggestion 3

def solve():
    # h1, h2, h3, w1, w2, w3 = map(int, input().split())
    h1, h2, h3, w1, w2, w3 = 3, 4, 6, 3, 3, 7
    # h1, h2, h3, w1, w2, w3 = 3, 4, 5, 6, 7, 8
    # h1, h2, h3, w1, w2, w3 = 5, 13, 10, 6, 13, 9
    # h1, h2, h3, w1, w2, w3 = 20, 25, 30, 22, 29, 24

    # 1 <= h1, h2, h3, w1, w2, w3 <= 30
    # 3 <= h1, h2, h3, w1, w2, w3 <= 30

    # 縦横 3 × 3 のマス目に、以下の条件をすべて満たすように各マスに正の整数を 1 つずつ書きこむことを考えます。
    # i=1,2,3 について、上から i 行目に書きこんだ数の和が h_i になる。
    # j=1,2,3 について、左から j 列目に書きこんだ数の和が w_j になる。

    # 1 <= h1, h2, h3, w1, w2, w3 <= 30
    # 3 <= h1, h2, h3, w1, w2, w3 <= 30

    # 1 <= h1, h2, h3, w1, w2, w3 <= 30
    # 3 <= h1, h2, h3, w1, w2, w3 <= 30

    # 1 <= h1, h2, h3, w1, w2, w3 <=

=======
Suggestion 4

def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    if h1+h2+h3 == w1+w2+w3:
        print(1)
    else:
        print(0)
main()

=======
Suggestion 5

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    ans += h1 * w1
    ans += h2 * w2
    ans += h3 * w3
    print(ans)

=======
Suggestion 6

def main():

    # 標準入力から値を取得する
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    # 条件を満たす書き込み方のパターン数を出力する
    print(h1*h2*h3*w1*w2*w3)

=======
Suggestion 7

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for i in range(1, 100):
        if (h1 + h2 + h3) % i != 0:
            continue
        for j in range(1, 100):
            if (w1 + w2 + w3) % j != 0:
                continue
            if (h1 + h2 + h3) // i != (w1 + w2 + w3) // j:
                continue
            if i * j <= h1 + h2 + h3:
                ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print(1)

=======
Suggestion 9

def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    #print(h1,h2,h3,w1,w2,w3)
    #h1+h2+h3 = h
    #w1+w2+w3 = w
    #h1+h2 = h-w3
    #h1+h3 = h-w2
    #h2+h3 = h-w1
    #w1+w2 = w-h3
    #w1+w3 = w-h2
    #w2+w3 = w-h1
    #h1+h2 = w1+w2
    #h1+h3 = w1+w3
    #h2+h3 = w2+w3
    #h1+h2+h3 = w1+w2+w3
    #h1+h2+h3 = h+w
    #h-w = w-h

=======
Suggestion 10

def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)
