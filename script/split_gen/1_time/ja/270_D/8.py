def main():
    #入力
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    #最初の山の石の数を変数に代入
    stone = n
    #高橋君が取り除く石の数を変数に代入
    takahashi = 0
    #青木君が取り除く石の数を変数に代入
    aoki = 0
    #高橋君が取り除く石の数を増やす
    for i in range(k):
        takahashi += a[i]
        #青木君が取り除く石の数を増やす
        for j in range(i,k):
            aoki += a[j]
            #高橋君が取り除く石の数が青木君が取り除く石の数より大きい場合
            if takahashi > aoki:
                #青木君が取り除く石の数を増やす
                aoki += a[j]
            #高橋君が取り除く石の数が青木君が取り除く石の数より小さい場合
            elif takahashi < aoki:
                #高橋君が取り除く石の数を増やす
                takahashi += a[i]
            #高橋君が取り除く石の数が青木君が取り除く石の数と同じ場合
            else:
                #青木君が取り除く石の数を増やす
                aoki += a[j]
    #高橋君が取り除く石の数を出力
    print(takahashi)
