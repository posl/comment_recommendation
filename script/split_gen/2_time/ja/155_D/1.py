def main():
    # N個の整数A1,A2,...,ANがあります。
    # このうち2つを選んでペアにする方法は((N(N-1))/(2))通りありますが、それぞれのペアについて積を求め、小さい順に並べ替えたとき、K番目にくる数は何になるでしょう？
    # 制約
    # 入力はすべて整数
    # 2 ≦ N ≦ 2 × 10^5
    # 1 ≦ K ≦ ((N(N-1))/(2))
    # -10^9 ≦ Ai ≦ 10^9 (1 ≦ i ≦ N)
    # 入力
    # 入力は以下の形式で標準入力から与えられる。
    # N K
    # A1 A2 ... AN
    # 出力
    # 答えを出力せよ。
    # 入力例 1
    # 4 3
    # 3 3 -4 -2
    # 出力例 1
    # -6
    # ペアの組み方は6通りあり、それぞれの積は9, -12, -6, -12, -6, 8です。
    # 小さい順に並べ替えると-12, -12, -6, -6, 8, 9となり、3番目にくる数は-6です。
    # 入力例 2
    # 10 40
    # 5 4 3 2 -1 0 0 0 0 0
    # 出力例 2
    # 6
    # 入力例 3
    # 30 413
    # -170202098 -268409015 537203564 983211703 21608710 -443999067 -937727165 -97596546 -372334013 398994917 -972141167 798607104 -949
