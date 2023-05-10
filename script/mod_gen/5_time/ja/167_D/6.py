def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,K,A)
    #テレポートの移動先を格納するリスト
    teleport = [1]
    #テレポートの移動先を格納するリストのインデックス
    teleport_index = 0
    #テレポートの移動先を格納するリストの長さ
    teleport_len = 1
    #移動回数
    move_count = 0
    #移動先が変わらない場合のループ回数
    loop_count = 0
    #移動先が変わらない場合のループ回数
    loop_count_max = 0
    #テレポートの移動先を格納するリストの長さがNになるまでループ
    while teleport_len < N:
        #テレポートの移動先を格納するリストの長さがNになるまでループ
        while teleport_len < N:
            #テレポートの移動先を格納するリストのインデックスが移動回数より大きい場合
            if teleport_index > move_count:
                #移動回数をインクリメント
                move_count += 1
                #ループ回数をリセット
                loop_count = 0
                #テレポートの移動先を格納するリストのインデックスをリセット
                teleport_index = 0
                #テレポートの移動先を格納するリストの長さをリセット
                teleport_len = 1
                #テレポートの移動先を格納するリストをリセット
                teleport = [1]
                #print("move_count:",move_count)
                #print("teleport_index:",teleport_index)
                #print("teleport_len:",teleport_len)
                #print("teleport:",teleport)
                break
            #テレポートの移動先を格納するリ

if __name__ == '__main__':
    main()