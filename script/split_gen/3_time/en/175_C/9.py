def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    # 1. xがdより小さい場合はx - d*kの絶対値を出力
    if x < d:
        print(abs(x - d*k))
        return
    # 2. xがdより大きい場合は、xをdで割った余りを出力
    if x >= d:
        if x % d > 0:
            if k % 2 == 0:
                print(x % d)
                return
            else:
                print(abs((x % d) - d))
                return
        else:
            if k % 2 == 0:
                print(x % d)
                return
            else:
                print(abs((x % d) - d))
                return
