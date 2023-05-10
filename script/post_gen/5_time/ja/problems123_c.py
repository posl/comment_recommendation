Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = int(input())
    B = int(input())

=======
Suggestion 2

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(N,A,B,C,D,E)
    #print(type(N),typ

=======
Suggestion 3

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    print(5 + (N - 1) // min(A, B, C, D, E))

=======
Suggestion 4

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_num = min(A,B,C,D,E)
    if N % min_num == 0:
        time = N // min_num
    else:
        time = N // min_num + 1
    print(time + 4)

=======
Suggestion 5

def main():
    # ここに書く
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    # 1. 都市1にN人がいる
    # 2. 都市1から2へは電車で1分で移動する。1つの電車にはA人まで乗ることができる。
    # 3. 都市2から3へはバスで1分で移動する。1つのバスにはB人まで乗ることができる。
    # 4. 都市3から4へはタクシーで1分で移動する。1つのタクシーにはC人まで乗ることができる。
    # 5. 都市4から5へは飛行機で1分で移動する。1つの飛行機にはD人まで乗ることができる。
    # 6. 都市5から6へは船で1分で移動する。1つの船にはE人まで乗ることができる。
    # 7. 全員が都市6に到着するまでに最短で何分かかるでしょうか？
    # 8. 乗り継ぎにかかる時間を考える必要はありません。
    # 9. 全員が都市6に移動するのに必要な最小の時間を分単位で出力せよ。
    # 10. 入力は以下の形式で標準入力から与えられる。
    # 11. N
    # 12. A
    # 13. B
    # 14. C
    # 15. D
    # 16. E
    # 17. 1 ≦ N, A, B, C,

=======
Suggestion 6

def solve():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    ans = (N-1)//min(A,B,C,D,E)+1 + 4
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((N-1)//min(A,B,C,D,E)+5)

=======
Suggestion 8

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    ans = N // min(A, B, C, D, E)
    if N % min(A, B, C, D, E) != 0:
        ans += 1
    ans += 4
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    ans = 0
    ans += (N + A - 1) // A
    ans += (N + B - 1) // B
    ans += (N + C - 1) // C
    ans += (N + D - 1) // D
    ans += (N + E - 1) // E
    ans += 4
    print(ans)
main()

=======
Suggestion 10

def main():
    # 標準入力の取得
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    # 処理
    # 最小公倍数を求める
    # 最小公倍数を求める関数
    def lcm(x, y):
        return (x * y) // gcd(x, y)
    # 最大公約数を求める関数
    def gcd(x, y):
        if x < y:
            x, y = y, x
        while y > 0:
            x, y = y, x % y
        return x

    # 最小公倍数を求める
    lcm_ab = lcm(a, b)
    lcm_cd = lcm(c, d)
    lcm_abcde = lcm(lcm_ab, lcm_cd)
    lcm_abcde = lcm(lcm_abcde, e)

    # 答え
    ans = (n + lcm_abcde - 1) // lcm_abcde

    # 結果の出力
    print(ans)
