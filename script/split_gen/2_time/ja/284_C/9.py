def main():
    import sys
    import numpy as np
    import itertools
    from collections import deque
    #入力
    N, M = map(int, input().split())
    #グラフの初期化
    G = np.zeros((N, N), dtype=np.int)
    #グラフの作成
    for i in range(M):
        u_i, v_i = map(int, input().split())
        G[u_i-1, v_i-1] = 1
        G[v_i-1, u_i-1] = 1
    #print(G)
    #連結成分の個数
    cnt = 0
    #探索済みの頂点を記録するリスト
    checked = []
    #全ての頂点を探索する
    for i in range(N):
        #探索済みの頂点はスキップ
        if i in checked:
            continue
        #探索済みの頂点に追加
        checked.append(i)
        #探索対象の頂点を記録するキュー
        q = deque([i])
        #キューが空になるまで探索
        while q:
            #キューから頂点を取り出す
            v = q.popleft()
            #頂点vに隣接する頂点を探索
            for j in range(N):
                #vと隣接する頂点で探索済みの頂点はスキップ
                if j in checked:
                    continue
                #vと隣接する頂点で探索済みの頂点でない場合
                if G[v, j] == 1:
                    #探索済みの頂点に追加
                    checked.append(j)
                    #キューに追加
                    q.append(j)
        #連結成分の個数をカウントアップ
        cnt += 1
    #出力
    print(cnt)
