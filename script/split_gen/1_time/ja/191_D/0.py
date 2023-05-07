def main():
    import sys
    import math
    from decimal import Decimal
    # 標準入力
    #X, Y, R = map(float, input().split())
    X, Y, R = map(Decimal, input().split())
    #print(X, Y, R)
    # 10^5倍
    #X = X * 100000
    #Y = Y * 100000
    #R = R * 100000
    X = X * 10000
    Y = Y * 10000
    R = R * 10000
    #print(X, Y, R)
    # 原点を中心とした円の内部または周上にある格子点の個数
    # 原点を中心とした円の内部または周上にある格子点の
