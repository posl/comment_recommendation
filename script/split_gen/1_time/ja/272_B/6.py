def main():
    N, M = map(int, input().split())
    # 1 人目から N 人目までの人が 1 回も参加していない状態で初期化
    # 0 は参加していないことを意味する
    people = [[0] * M for _ in range(N)]
    for i in range(M):
        # 参加人数 k_i と参加者の番号 x_{i,1} x_{i,2} ... x_{i,k_i} を取得
        k_i, *x_i = map(int, input().split())
        for j in range(k_i):
            # 参加している人の人数の配列の i 番目の要素を 1 にする
            people[x_i[j] - 1][i] = 1
    # 2 重ループでどの二人も少なくとも 1 回同じ舞踏会に参加しているか調べる
    for i in range(N - 1):
        for j in range(i + 1, N):
            # どの舞踏会にも参加していない場合は No を出力して終了
            if sum([people[i][k] & people[j][k] for k in range(M)]) == 0:
                print("No")
                return
    # どの二人も少なくとも 1 回同じ舞踏会に参加している場合は Yes を出力
    print("Yes")
main()
