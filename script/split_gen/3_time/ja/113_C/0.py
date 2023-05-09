def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for i in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    P = np.array(P)
    Y = np.array(Y)
    #県ごとに市の誕生年をソート
    Y_sort = np.argsort(Y[P-1])
    #県ごとに市の誕生年の順位を格納
    Y_rank = np.zeros(M, dtype=np.int64)
    for i in range(N):
        Y_rank[P-1==i] = np.arange(1, np.sum(P-1==i)+1)
    #県と市の順位を合わせて6桁になるように0埋め
    ans = np.char.zfill(np.array(P, dtype=np.str), 6) + np.char.zfill(np.array(Y_rank, dtype=np.str), 6)
    #出力
    for i in ans:
        print(i)
