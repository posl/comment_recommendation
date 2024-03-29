def main():
    X = input()
    M = int(input())
    # X の最大の数字を求める
    d = 0
    for c in X:
        d = max(d, int(c))
    # X が 1 桁のときは M 以下の値が 1 つだけ存在する
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    # X が 2 桁以上のときは、d+1 以上の整数 n で X を n 進法表記の数とみなして得られる値のうち、M 以下であるようなものの数を求める
    # この値は d+1 以上 M 以下の整数のうち、d+1 以上の整数 n で X を n 進法表記の数とみなして得られる値のうち、M 以下であるようなものの数と等しい
    # そのため、d+1 以上 M 以下の整数のうち、X を d+1 以上の整数 n で n 進法表記の数とみなして得られる値のうち、M 以下であるようなものの数を求めればよい
    # X を d+1 以上の整数 n で n 進法表記の数とみなして得られる値のうち、M 以下であるようなものの数を求めるには、二分探索を用いる
    # 二分探索の範囲を [d+1, M] とする
    # 二分探索の中央の値 n で X を n 進法表記の数とみなして得られる値を求め、M 以下であるかどうかを判定する
    # このとき、X を n 進法表

if __name__ == '__main__':
    main()