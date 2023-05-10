def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #処理
    #アメーバの親子関係を辞書で表現
    dic = {}
    for i in range(1, N+1):
        dic[i] = [A[i-1], 2*i, 2*i+1]
    #print(dic)
    #アメーバの親子関係を辿り、アメーバ1までの距離を記録
    #親子関係を辿るためのキュー
    queue = []
    #アメーバ1からの距離を記録するリスト。アメーバ1は0
    dist = [0 for i in range(2*N+1)]
    #アメーバ1からの距離を記録するリストに、アメーバ1から距離1のアメーバを追加
    queue.append(1)
    #print(queue)
    #print(dist)
    #アメーバ1からの距離を記録するリストに、アメーバ1から距離1のアメーバを追加
    while len(queue) > 0:
        #キューの先頭のアメーバを取り出す
        ame = queue.pop(0)
        #print(ame)
        #アメーバameの親子関係を調べる
        for i in range(1, 4):
            #アメーバameのi番目の子アメーバを取得
            child = dic[ame][i-1]
            #print(child)
            #アメーバameのi番目の子アメーバが、アメーバ1からの距離を記録するリストに未登録の場合
            if dist[child] == 0:
                #アメーバameのi番目の子アメーバの距離を記録するリストに、アメ

if __name__ == '__main__':
    main()