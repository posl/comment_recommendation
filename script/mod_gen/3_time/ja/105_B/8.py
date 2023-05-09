def main():
    N = int(input())
    # N = 11
    # N = 40
    # N = 3
    # 1 個 4 ドルのケーキと 1 個 7 ドルのドーナツの合計金額が N ドルとなる買い方があるかどうかを判定する
    # 4 ドルのケーキを i 個, 7 ドルのドーナツを j 個買うと, 合計金額は 4 × i + 7 × j ドルとなる
    # 4 × i + 7 × j = N となる i, j を求める
    # 4 × i + 7 × j = N
    # 7 × j = N - 4 × i
    # j = (N - 4 × i) / 7
    # 7 × j が整数かどうかで判定する
    for i in range(0, N + 1):
        if (N - 4 * i) % 7 == 0:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()