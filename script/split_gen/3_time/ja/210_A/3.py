def main():
    #入力
    N,A,X,Y = map(int,input().split())
    #処理
    if N <= A:
        ans = X * N
    else:
        ans = X * A + Y * (N - A)
    
    #出力
    print(ans)
