def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    # P = (2,3,1,4) なので、P_2 = 3 です。したがって、2 を出力します。
    # P = (3,5,1,4,2) なので、P_5 = 2 です。したがって、5 を出力します。
    # P = (1,2,3,4,5,6) なので、P_6 = 6 です。したがって、6 を出力します。
    # p.index(x) で、x のインデックスを取得
    print(p.index(x) + 1)
