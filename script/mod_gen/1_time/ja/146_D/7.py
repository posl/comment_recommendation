def main():
    #入力
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N-1)]
    #print(N)
    #print(ab)
    #グラフを作成
    G = [[] for _ in range(N+1)]
    for a, b in ab:
        G[a].append(b)
        G[b].append(a)
    #print(G)
    #深さ優先探索
    #深さ優先探索の実装
    def dfs(v, p, d):
        #print(v, p, d)
        #頂点vを訪れたことを記録
        seen[v] = 1
        #頂点vの深さを記録
        depth[v] = d
        #頂点vに隣接する頂点を探索
        for nv in G[v]:
            #頂点vに隣接する頂点nvが親頂点pでない場合
            if nv != p:
                #頂点nvが未訪問の場合
                if seen[nv] == 0:
                    #頂点nvを訪問済みにする
                    seen[nv] = 1
                    #頂点nvの深さを記録
                    depth[nv] = d + 1
                    #頂点vを親頂点として頂点nvを再帰的に探索
                    dfs(nv, v, d + 1)
                #頂点nvが訪問済みの場合
                else:
                    #頂点nvの深さを記録
                    depth[nv] = d - 1
    #深さ優先探索を実行
    #頂点1を根とする木を探索
    #頂点iを訪れたかどうかを記録する配列
    seen = [0] * (N+1)
    #頂点iの深さを記録する配列
    depth = [

if __name__ == '__main__':
    main()