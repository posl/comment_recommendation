def main():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, M, T)
    #print(A)
    #print(B)
    #バッテリー残量
    battery = N
    #外出時刻
    out = 0
    #帰宅時刻
    home = T
    #カフェに滞在している間にバッテリーが増える
    for i in range(M):
        #外出時刻からカフェに滞在開始時刻までの間にバッテリーが減る
        battery -= A[i] - out
        #バッテリーが減り切ったらNo
        if battery <= 0:
            print("No")
            return
        #バッテリーが減り切らなかったらバッテリーが増える
        else:
            battery += A[i] - out
            #バッテリーが増え過ぎないように調整
            if battery >= N:
                battery = N
            #カフェに滞在開始時刻からカフェに滞在終了時刻までの間にバッテリーが増える
            battery += B[i] - A[i]
            #バッテリーが増え過ぎないように調整
            if battery >= N:
                battery = N
            #外出時刻をカフェに滞在終了時刻に更新
            out = B[i]
    #バッテリーが減り切ったらNo
    battery -= home - out
    if battery <= 0:
        print("No")
        return
    #バッテリーが減り切らなかったらYes
    else:
        print("Yes")
        return

if __name__ == '__main__':
    main()