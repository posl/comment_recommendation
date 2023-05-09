def solve():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    # 各ラウンドの勝敗を記録
    # 1ラウンド目：[0,0,0,0]
    # 2ラウンド目：[0,0,0,0]
    # 3ラウンド目：[0,0,0,0]
    win = [ [0]*2*N for _ in range(M) ]
    # 各ラウンドの順位を記録
    # 1ラウンド目：[0,1,2,3]
    # 2ラウンド目：[0,1,2,3]
    # 3ラウンド目：[0,1,2,3]
    rank = [ [i for i in range(2*N)] for _ in range(M) ]
    # 1ラウンド目の勝敗を記録
    for i in range(2*N):
        for j in range(M):
            if A[i][j] == "G":
                if A[i+1][j] == "C":
                    win[j][i] = 1
                elif A[i+1][j] == "P":
                    win[j][i+1] = 1
            elif A[i][j] == "C":
                if A[i+1][j] == "P":
                    win[j][i] = 1
                elif A[i+1][j] == "G":
                    win[j][i+1] = 1
            elif A[i][j] == "P":
                if A[i+1][j] == "G":
                    win[j][i] = 1
                elif A[i+1][j] == "C":
                    win[j][i+1] = 1
    # 2ラウンド目以降の勝敗を記録
    for j in range(1,M):
        # 1位と2位の勝敗を記録
        for i in range(0,2*N,2):
            if win[j-1][rank[j-1][
