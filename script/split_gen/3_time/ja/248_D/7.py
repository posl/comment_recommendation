def main():
    #数列の長さ
    N=int(input())
    #数列
    A=list(map(int,input().split()))
    #クエリの数
    Q=int(input())
    #クエリの処理
    for i in range(Q):
        #クエリの受け取り
        L,R,X=map(int,input().split())
        #数列の切り出し
        A_slice=A[L-1:R]
        #数列の切り出した部分の中でXと同じ値の個数をカウント
        count=A_slice.count(X)
        #出力
        print(count)
