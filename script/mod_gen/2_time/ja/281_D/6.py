def main():
    #入力
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    #Aの要素をDで割った余りを求める
    B = [a % D for a in A]
    #Bの要素の和を求める
    total = sum(B)
    #KがNより大きい場合、-1を出力
    if K > N:
        print(-1)
        return
    #KがDの倍数でない場合、-1を出力
    if K % D != 0:
        print(-1)
        return
    #Bの要素の和がKの倍数でない場合、-1を出力
    if total % K != 0:
        print(-1)
        return
    #Bの要素の和をKで割った商を求める
    div = total // K
    #Bの要素の和をKで割った商をDで割った商を求める
    div2 = div // D
    #Bの要素の和をKで割った商をDで割った余りを求める
    mod = div % D
    #Bの要素の和をKで割った商をDで割った商を出力
    print(div2)
    #Bの要素の和をKで割った商をDで割った余りが0でない場合
    if mod != 0:
        #Bの要素の和をKで割った商をDで割った商にDを足す
        div2 += D
    #Bの要素の和をKで割った商をDで割った商をK-1個出力
    print(*([div2] * (K - 1)), sep=" ")

if __name__ == '__main__':
    main()