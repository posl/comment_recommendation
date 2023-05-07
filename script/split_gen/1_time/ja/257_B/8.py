def main():
    N, K, Q = map(int,input().split())
    A = list(map(int,input().split()))
    L = list(map(int,input().split()))
    #K個のコマの位置を記録するリスト
    #コマの位置は1～Nの範囲であるため、インデックスとコマの位置を対応させるために0を追加
    #例：コマの位置が2の場合、2番目の要素に1を代入
    pos = [0] * (N+1)
    for i in range(K):
        pos[A[i]] = 1
    #Q回の操作を行う
    for i in range(Q):
        #左からL_i番目のコマが一番右のマスにあるか
        if L[i] == K:
            continue
        #左からL_i番目のコマがあるマスの1つ右のマスにコマが無いか
        if pos[L[i]+1] == 0:
            #コマを1つ右のマスに移動させる
            pos[L[i]+1] = 1
            pos[L[i]] = 0
        else:
            continue
    #コマの位置を出力する
    for i in range(1,N+1):
        if pos[i] == 1:
            print(i,end=" ")
    print()
