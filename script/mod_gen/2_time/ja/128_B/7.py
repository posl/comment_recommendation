def main():
    N = int(input())
    # N 個のレストランの情報を格納するリスト
    rest_list = []
    for i in range(N):
        # S_i 市にあり、あなたは 100 点満点中 P_i 点と評価しています。
        S_i, P_i = input().split()
        rest_list.append([i+1, S_i, int(P_i)])
    # 1.市名が辞書順で早いものから紹介していく。
    # 2.同じ市に複数レストランがある場合は、点数が高いものから紹介していく。
    rest_list.sort(key=lambda x: (x[1], -x[2]))
    # N 行出力せよ。i 行目 (1 ≤ i ≤ N) には、i 番目に紹介されるレストランの番号を出力せよ。
    for rest in rest_list:
        print(rest[0])

if __name__ == '__main__':
    main()