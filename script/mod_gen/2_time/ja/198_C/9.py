def main():
    import sys
    import math
    # 標準入力
    r, x, y = map(int, sys.stdin.readline().split())
    # 処理
    # 1歩で移動できる距離
    r1 = math.sqrt(x**2 + y**2)
    if r1 == r:
        print(1)
    elif r1 <= r*2:
        print(2)
    else:
        print(math.ceil(r1/r))

if __name__ == '__main__':
    main()