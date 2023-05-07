def main():
    # input
    As = [int(input()) for _ in range(5)]
    # compute
    # 10の倍数に切り上げる
    As = [((a+9)//10)*10 for a in As]
    # 最小値を求める
    m = min(As)
    # 最小値の10の倍数の差分を求める
    d = m - As[0]
    # 最小値の10の倍数に合わせる
    As = [a+d for a in As]
    # 最大値を求める
    M = max(As)
    # 最大値に合わせる
    As = [M for _ in range(5)]
    # output
    print(sum(As))

if __name__ == '__main__':
    main()