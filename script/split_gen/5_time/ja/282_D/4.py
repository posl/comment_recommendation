def main():
    N, M = map(int, input().split())
    #print(N, M)
    edge_list = [list(map(int, input().split())) for _ in range(M)]
    #print(edge_list)
    #print(len(edge_list))
    #print(edge_list[0])
    #print(edge_list[0][0])
    #print(edge_list[0][1])
    #print(len(edge_list[0]))
    #print(edge_list[0][0]-1)
    #print(edge_list[0][1]-1)
    # N個の頂点と M本の辺からなる単純な無向グラフGがある
    # i=1,2,...,Mについて、i番目の辺は頂点u_iと頂点v_iを結ぶ
    # 1 ≦ u < v ≦ Nを満たす整数の組(u,v)であって、
    # 2つの条件をともに満たすものの個数を出力
    # 1. グラフGにおいて、頂点uと頂点vを結ぶ辺は存在しない
    # 2. グラフGに、頂点uと頂点vを結ぶ辺を追加して得られるグラフは二部グラフである
    # 二部グラフとは？
    # 無向グラフが二部グラフであるとは、
    # 各頂点を黒または白のどちらかの色で塗ることができることを言います。
    # 同じ色に塗られた頂点どうしを結ぶ辺は存在しない。
    # 二部グラフであるかどうかを判定する
    # 1. 頂点の色を塗る
    # 2. 同じ色に塗られた頂点どうしを結ぶ辺が存在するかを
