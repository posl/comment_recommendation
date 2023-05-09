def main():
    A, B, C, D = map(int, input().split())
    # A以上B以下の整数の和が素数であるかどうかを判定する
    # A以上B以下の整数の和は、
    # 1以上B以下の整数の和から1以上A-1以下の整数の和を引けば求めることができる
    # 1以上B以下の整数の和は、
    # B以下の素数の個数にBを掛けたものに、
    # B以下の合成数の個数にBを掛けたものを加えたものになる
    # つまり、B以下の合成数の個数を求めれば良い
    # 1以上B以下の合成数の個数は、
    # 1以上B以下の整数のうち、B以下の素数の倍数の個数に、
    # 1以上B以下の整数のうち、B以下の素数の2乗以上の倍数の個数を加えたものになる
    # つまり、B以下の素数の倍数の個数とB以下の素数の2乗以上の倍数の個数を求めれば良い
    # 1以上B以下の素数の倍数の個数は、
    # B以下の素数の個数にB以下の素数の個数を掛けたものになる
    # つまり、B以下の素数の個数を求めれば良い
    # 1以上B以下の素数の個数は、
    # B以下の素数のリストの長さになる
    # 1以上B以下の素数のリストを求めるにはエラトステネスの篩を使う
    # 1以上B以下の素数の2乗以上の倍数の個数は、
    # B
