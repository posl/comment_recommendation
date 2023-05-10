def main():
    X, Y = map(int, input().split())
    MOD = 10**9+7
    if (X+Y)%3 != 0:
        print(0)
        return
    # 2x+y = X
    # x+2y = Y
    # 2x+y = x+2y
    # x = y
    # 3x = X
    # x = X/3
    # 3y = Y
    # y = Y/3
    # x+y = X/3+Y/3 = (X+Y)/3 = N
    N = (X+Y)//3
    if X < N or Y < N:
        print(0)
        return
    # XとYの差の絶対値が3の倍数でなければならない
    if abs(X-Y)%3 != 0:
        print(0)
        return
    # (N, N)に行く方法は、
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせの数
    # (N, N)に行く方法は、
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせの数
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせの数
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせの数
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせの数
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせ

if __name__ == '__main__':
    main()