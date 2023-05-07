def main():
    #入力
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #Aの値を変えないようにコピー
    A_copy = A.copy()
    #コマを動かす
    for i in range(Q):
        #動かすコマの番号
        L_i = L[i]
        #動かすコマの位置
        A_i = A[L_i-1]
        #最後のコマでなければ
        if A_i != N:
            #コマの右にコマがなければ
            if A_i+1 not in A:
                #コマを右に移動
                A[L_i-1] += 1
                #移動したコマの左のコマを右に移動
                if A_i-1 in A:
                    A[A.index(A_i-1)] += 1
    #出力
    for i in range(K):
        print(A[i], end=" ")
