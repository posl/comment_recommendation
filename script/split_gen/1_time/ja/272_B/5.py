def main():
    N, M = map(int, input().split())
    # 0 で初期化した N×N の行列を作成
    # 0 は参加していないことを示す
    # 1 は参加していることを示す
    # 今回は 0 と 1 だけを使うので、bool ではなく int を使っても良い
    # 2 は人 i と人 j が共に参加していることを示す
    # これは最後に出力する際に使う
    # 0 と 1 は入力の際に使う
    # 2 は出力の際に使う
    table = [[0 for i in range(N)] for j in range(N)]
    
    for i in range(M):
        # 1 回目の舞踏会の参加者数
        k = int(input())
        # 1 回目の舞踏会の参加者の番号
        x = list(map(int, input().split()))
        for j in range(k):
            for l in range(j+1, k):
                # 参加している人同士に 2 を代入
                table[x[j]-1][x[l]-1] = 2
                table[x[l]-1][x[j]-1] = 2
    
    for i in range(N):
        for j in range(N):
            # 2 があれば Yes を出力
            if table[i][j] == 2:
                print("Yes")
                return
    
    # 2 がなければ No を出力
    print("No")
