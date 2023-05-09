def main():
    N, A, B = map(int, input().split())
    # 1 から N までの整数のうち、A または B で割り切れない整数の和を求める
    # A で割り切れる整数の個数
    cntA = N // A
    # B で割り切れる整数の個数
    cntB = N // B
    # A と B で共通に割り切れる整数の個数
    cntAB = N // (A * B)
    # 1 から N までの整数のうち、A または B で割り切れない整数の個数
    cnt = N - cntA - cntB + cntAB
    print(cnt * (A + B) - cntAB * A * B)
