def main():
    N, M = map(int, input().split())
    A = [input() for i in range(2*N)]
    # 1ラウンド目
    win = [0] * (2*N)
    for i in range(N):
        if A[2*i+1][0] == "G" and A[2*i][0] == "C":
            win[2*i] += 1
        elif A[2*i+1][0] == "C" and A[2*i][0] == "P":
            win[2*i] += 1
        elif A[2*i+1][0] == "P" and A[2*i][0] == "G":
            win[2*i] += 1
        else:
            win[2*i+1] += 1
    # 2ラウンド目以降
    for i in range(M-1):
        # 勝ち数でソート
        sort_win = sorted(range(2*N), key=lambda x: win[x], reverse=True)
        # 順位を入れ替え
        for j in range(N):
            if A[sort_win[2*j+1]][i+1] == "G" and A[sort_win[2*j]][i+1] == "C":
                win[sort_win[2*j+1]] += 1
            elif A[sort_win[2*j+1]][i+1] == "C" and A[sort_win[2*j]][i+1] == "P":
                win[sort_win[2*j+1]] += 1
            elif A[sort_win[2*j+1]][i+1] == "P" and A[sort_win[2*j]][i+1] == "G":
                win[sort_win[2*j+1]] += 1
            else:
                win[sort_win[2*j]] += 1
    # 結果出力
    for i in range(2*N):
        print(win.index(i)+1)
main()
問題文
高橋君は、あるゲームのプレイヤーです。このゲームは N 個のマスからなる
