def solve():
    # 標準入力からデータを取得する
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    # ここに、プログラムを追記
    # 各リールの表示文字を保持する
    reel = [0] * N
    for i in range(N):
        reel[i] = S[i][0]
    # 各リールの表示文字を揃えるために必要な時間を計算する
    time = 0
    for i in range(N):
        # 各リールの表示文字を揃えるために必要な時間を計算する
        # 各リールの表示文字を揃えるために必要な時間は、
        # (10 - (reel[i] - S[i][0])) % 10
        # となる
        time += (10 - (int(reel[i]) - int(S[i][0]))) % 10
        # 各リールの表示文字を更新する
        reel[i] = S[i][0]
    # 各リールを止めるために必要な時間を計算する
    for i in range(1, N):
        # 各リールを止めるために必要な時間は、
        # 10 * (len(S[i]) - 1)
        # となる
        time += 10 * (len(S[i]) - 1)
    # 結果を出力する
    print(time)
