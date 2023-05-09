def main():
    # 標準入力の受け取り
    # 9行の文字列を受け取り、リストに格納
    S = []
    for i in range(9):
        S.append(input())
    #print(S)
    # ポーンが置かれている座標のリストを作成
    p_list = []
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                p_list.append([i,j])
    #print(p_list)
    # 4頂点の組み合わせを全て試して、4頂点全てにポーンが置かれているかを確認
    # 4頂点全てにポーンが置かれている正方形の個数をカウント
    count = 0
    for i in range(len(p_list)):
        for j in range(i+1,len(p_list)):
            for k in range(j+1,len(p_list)):
                for l in range(k+1,len(p_list)):
                    # 4頂点の座標を取り出す
                    p1 = p_list[i]
                    p2 = p_list[j]
                    p3 = p_list[k]
                    p4 = p_list[l]
                    #print(p1,p2,p3,p4)
                    # 4頂点全てにポーンが置かれているかを確認
                    if p1[0] == p2[0] and p1[1] == p4[1] and p3[0] == p4[0] and p2[1] == p3[1]:
                        count += 1
    #print(count)
    # 答えを出力
    print(count)
