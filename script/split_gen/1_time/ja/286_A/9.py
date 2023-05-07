def main():
    #入力
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,P,Q,R,S)
    #print(A)
    #処理
    #数列 A の P 番目から Q 番目の項までと R 番目から S 番目の項までを入れ替えた数列を B=(B_1, B_2,..., B_N) とします。
    #数列 B を出力してください。
    #B = A[0:P-1] + A[Q:R-1] + A[S:N]
    B = A[0:P-1] + A[Q:R-1] + A[S:N]
    #出力
    print(B)
