def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    # 各ラウンドの勝者を保存するリスト
    win = [0 for _ in range(2*N)]
    # 各ラウンドの勝者を保存するリスト
    win = [0 for _ in range(2*N)]
    # 1ラウンド目
    for i in range(0, 2*N, 2):
        if A[i][0] == A[i+1][0]:
            # 引き分けの場合は、勝者を保存しない
            continue
        elif (A[i][0] == 'G' and A[i+1][0] == 'C') or (A[i][0] == 'C' and A[i+1][0] == 'P') or (A[i][0] == 'P' and A[i+1][0] == 'G'):
            # 勝ちの場合は、勝者を保存する
            win[i] = 1
        else:
            # 負けの場合は、勝者を保存する
            win[i+1] = 1
    # 2ラウンド目以降
    for i in range(1, M):
        # 各ラウンドの勝者を保存するリスト
        next_win = [0 for _ in range(2*N)]
        for j in range(0, 2*N, 2):
            # 各ラウンドの勝者を保存するリスト
            next_win = [0 for _ in range(2*N)]
            for j in range(0, 2*N, 2):
                # 前ラウンドの勝者がいない場合は、勝者を保存しない
                if win[j] == 0 and win[j+1] == 0:
                    continue
                # 前ラウンドの勝者がいる場合は、勝者を保存する
                if win[j] == 1:
                    if A[j][i] == A[j+1][i]:
