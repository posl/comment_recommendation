def main():
    L, Q = map(int, input().split())
    C = []
    X = []
    for i in range(Q):
        c, x = map(int, input().split())
        C.append(c)
        X.append(x)
    #木材の長さを格納するリスト
    wood = [L]
    #木材の長さの累積和を格納するリスト
    wood_sum = [0]
    for i in range(Q):
        if C[i] == 1:
            #木材の長さの累積和を計算
            #木材の長さの累積和は木材の長さのリストの累積和
            #木材の長さのリストの累積和は木材の長さの累積和を計算するために必要
            wood_sum.append(wood_sum[-1] + wood[-1])
            #木材の長さを更新
            #木材の長さのリストの累積和を計算するために必要
            #木材の長さのリストの累積和は木材の長さの累積和を計算するために必要
            #木材の長さの累積和を計算するために必要
            wood.append(X[i] - (wood_sum[-1] - wood_sum[-2]))
            #木材の長さを更新
            #木材の長さのリストの累積和を計算するために必要
            #木材の長さの累積和を計算するために必要
            wood.append(wood_sum[-1] + wood[-2] - X[i])
        elif C[i] == 2:
            #木材の長さの累積和を計算
            #木材の長さの累積和は木材の長さのリストの累積和

if __name__ == '__main__':
    main()