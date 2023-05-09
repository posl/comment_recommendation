def main():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    #隣接リスト
    adj = [[] for _ in range(N)]
    #隣接リスト作成
    for _ in range(N-1):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    #頂点 X から頂点 Y への単純パス上の頂点番号を順に空白区切りで出力せよ。
    #隣接リストを使って、BFSで探索する
    #探索は、Xからスタートして、Yに行くまでの探索である。
    #探索の経路を記録しておく。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探
