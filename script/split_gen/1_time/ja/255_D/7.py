def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    
    #Aの要素の最大値と最小値を求める
    min_A = min(A)
    max_A = max(A)
    
    #Aの要素の最大値と最小値の差を求める
    diff_A = max_A - min_A
    
    #Aの要素の最大値と最小値の差が0以下の場合
    if diff_A <= 0:
        #Qの要素の数だけ繰り返す
        for i in range(Q):
            #Xの要素の値を出力する
            print(X[i])
        return
    
    #Aの要素の最大値と最小値の差が1以上の場合
    #Aの要素の最大値と最小値の差を出力する
    print(diff_A)
    
    #Aの要素の最大値と最小値の差を求める
    diff_A = max_A - min_A
    
    #Aの要素の最大値と最小値の差が1以上の場合
    if diff_A > 0:
        #Aの要素の最大値と最小値の差を求める
        diff_A = max_A - min_A
        
        #Aの要素の最大値と最小値の差を出力する
        print(diff_A)
        
        #Aの要素の最大値と最小値の差を求める
        diff_A = max_A - min_A
        
        #Aの要素の最大値と最小値の差を出力する
        print(diff_A)
        
        #Aの要素の最大値と最小値の差を求める
        diff_A = max_A - min_A
        
        #Aの要素の最大値と最小値の差を出力する
