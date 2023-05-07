def main():
    #標準入力からKを取得
    K = int(input())
    #Kが2以上100以下の場合
    if 2 <= K and K <= 100:
        #偶数の数を格納する変数を定義
        even = 0
        #奇数の数を格納する変数を定義
        odd = 0
        #1からKまでの数を順に取得
        for i in range(1,K+1):
            #iが偶数の場合
            if i % 2 == 0:
                #偶数の数を1増やす
                even += 1
            #iが奇数の場合
            else:
                #奇数の数を1増やす
                odd += 1
        #偶数の数と奇数の数を掛け合わせた数を出力
        print(even * odd)
