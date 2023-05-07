def main():
    N = int(input())
    # 木を表す隣接リスト
    tree = [[] for _ in range(N)]
    # 隣接リストを作成
    for _ in range(N-1):
        u,v,w = map(int, input().split())
        tree[u-1].append((v-1,w))
        tree[v-1].append((u-1,w))
    
    # 頂点0を根として探索
    # 頂点0からの距離を管理するリスト
    dist = [0]*N
    # 頂点0を訪問済みとする
    visited = [True] + [False]*(N-1)
    # 訪問済みの頂点のリスト
    que = [0]
    # 訪問済みの頂点のリストを順番に処理
    while que:
        # 訪問済みの頂点のリストから頂点を取り出す
        v = que.pop()
        # 頂点vに隣接する頂点を順番に処理
        for w,d in tree[v]:
            # 頂点wが訪問済みの場合は処理しない
            if visited[w]:
                continue
            # 頂点wを訪問済みとする
            visited[w] = True
            # 頂点wを訪問済みの頂点のリストに追加
            que.append(w)
            # 頂点wの距離を計算
            dist[w] = dist[v] + d
    
    # 距離が偶数なら0, 奇数なら1を出力
    for d in dist:
        print(d%2)

if __name__ == '__main__':
    main()