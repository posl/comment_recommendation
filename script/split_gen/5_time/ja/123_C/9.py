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
