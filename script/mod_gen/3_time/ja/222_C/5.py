def main():
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(2*N)]
    #順位の初期化
    rank = list(range(2*N))
    #Mラウンド分の勝者を決める
    for i in range(M):
        #勝者と敗者を格納するリスト
        winner = []
        loser = []
        #N組の対戦を行う
        for j in range(N):
            #勝者の人の番号を格納する
            if A[rank[2*j]][i] == "G" and A[rank[2*j+1]][i] == "C":
                winner.append(rank[2*j])
                loser.append(rank[2*j+1])
            elif A[rank[2*j]][i] == "C" and A[rank[2*j+1]][i] == "P":
                winner.append(rank[2*j])
                loser.append(rank[2*j+1])
            elif A[rank[2*j]][i] == "P" and A[rank[2*j+1]][i] == "G":
                winner.append(rank[2*j])
                loser.append(rank[2*j+1])
            elif A[rank[2*j]][i] == A[rank[2*j+1]][i]:
                winner.append(rank[2*j])
                winner.append(rank[2*j+1])
            else:
                winner.append(rank[2*j+1])
                loser.append(rank[2*j])
        #勝者をリストの先頭に移動させる
        for k in loser:
            rank.remove(k)
        rank = winner + rank
    #順位を出力する
    for l in range(2*N):
        print(rank[l]+1)

if __name__ == '__main__':
    main()