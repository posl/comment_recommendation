def main():
    #入力
    N,P,Q,R,S=map(int,input().split())
    A=list(map(int,input().split()))
    #処理
    B=A[:P-1]+A[Q:R-1]+A[S:]+A[P-1:Q]+A[R-1:S]
    #出力
    print(*B)
