def main():
    N = int(input())
    c = input()
    # Rの数
    R = c.count('R')
    # Wの数
    W = c.count('W')
    # Rの数が少ないほう
    min = R if R < W else W
    # Rの数が多いほう
    max = R if R >= W else W
    # 連続するRの数
    cnt = 0
    # 連続するRの最大数
    max_cnt = 0
    # 連続するRの最大数を求める
    for i in range(N):
        if c[i] == 'R':
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 0
    if cnt > max_cnt:
        max_cnt = cnt
    # 結果を出力
    print(min + max - max_cnt)
main()

if __name__ == '__main__':
    main()