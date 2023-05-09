def main():
    #入力
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    #A,Bを昇順にソートする
    A.sort()
    B.sort()
    
    #Aの要素のインデックスを0で初期化する
    a = 0
    #Bの要素のインデックスを0で初期化する
    b = 0
    #差の絶対値の最小値を10^9で初期化する
    min = 10**9
    
    #Aの要素のインデックスがN-1より小さい間繰り返す
    while a < N-1:
        #Bの要素のインデックスがM-1より小さい間繰り返す
        while b < M-1:
            #Aの要素とBの要素の差の絶対値を求める
            x = abs(A[a] - B[b])
            #差の絶対値の最小値と比較する
            if x < min:
                #差の絶対値の最小値を更新する
                min = x
            #Bの要素のインデックスを1増やす
            b += 1
        #Bの要素のインデックスを0にする
        b = 0
        #Aの要素のインデックスを1増やす
        a += 1
    #差の絶対値の最小値を出力する
    print(min)

if __name__ == '__main__':
    main()