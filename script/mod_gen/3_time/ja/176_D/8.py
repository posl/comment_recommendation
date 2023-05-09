def main():
    H,W = map(int,input().split())
    Ch,Cw = map(int,input().split())
    Dh,Dw = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(list(input()))
    #print(H,W,Ch,Cw,Dh,Dw,S)
    #最短距離を求める
    #ワープ魔法で到達できる場合は、それを優先する
    #ワープ魔法で到達できない場合は、移動Aを優先する
    #ワープ魔法で到達できない場合は、移動Bを優先する
    #ワープ魔法の範囲
    warp = 2
    #ワープ魔法で移動するときの移動コスト
    warp_cost = 1
    #移動Aで移動するときの移動コスト
    moveA_cost = 1
    #移動Bで移動するときの移動コスト
    moveB_cost = 1
    #移動可能なマスのリスト
    move_list = []
    #ワープ魔法で移動可能なマスのリスト
    warp_list = []
    #ワープ魔法で移動可能なマスをリストに追加
    for i in range(1,H+1):
        for j in range(1,W+1):
            if abs(i-Ch) <= warp and abs(j-Cw) <= warp and S[i-1][j-1] == ".":
                warp_list.append([i,j])
    #print(warp_list)
    #移動可能なマスのリストを作成
    for i in range(1,H+1):
        for j in range(1,W+1):
            if S[i-1][j-1] == ".":
                move_list.append([i,j])
    #print(move_list)
    #最短距離を求める
    #ワープ魔法で

if __name__ == '__main__':
    main()