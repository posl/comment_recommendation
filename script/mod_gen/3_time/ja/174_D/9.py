def main():
    N = int(input())
    S = list(input())
    # 白い石の数
    white = S.count('W')
    # 赤い石の数
    red = N - white
    # 赤い石が左側にある場合
    left_red = 0
    # 赤い石が右側にある場合
    right_red = red
    # 赤い石が左側にある場合の最小操作回数
    left_min = 0
    # 赤い石が右側にある場合の最小操作回数
    right_min = 0
    for i in range(N):
        if S[i] == 'R':
            left_red += 1
            right_red -= 1
        else:
            left_min = max(left_min, left_red)
            right_min = max(right_min, right_red)
    print(min(left_min, right_min))

if __name__ == '__main__':
    main()