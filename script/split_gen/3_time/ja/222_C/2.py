def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    # 最終的な順位
    rank = list(range(1, 2*N+1))
    # Mラウンド目までの勝数
    win = [0]*2*N
    # 各ラウンドでの勝ち負け
    for i in range(M):
        # 各試合での勝ち負け
        for k in range(N):
            # 2k-1位の人と2k位の人が試合をする
            p1 = rank[2*k-1]-1
            p2 = rank[2*k]-1
            # 勝ち負けを判定
            if A[p1][i] == A[p2][i]:
                # 引き分け
                continue
            elif (A[p1][i] == 'G' and A[p2][i] == 'C') or \
                 (A[p1][i] == 'C' and A[p2][i] == 'P') or \
                 (A[p1][i] == 'P' and A[p2][i] == 'G'):
                # p1の勝ち
                win[p1] += 1
            else:
                # p2の勝ち
                win[p2] += 1
        # 勝数でソート
        rank = sorted(range(2*N), key=lambda x: (-win[x], x))
    # 結果出力
    for i in range(2*N):
        print(rank[i]+1)
