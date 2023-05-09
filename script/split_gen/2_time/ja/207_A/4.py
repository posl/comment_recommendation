def main():
    #入力
    A,B,C = map(int,input().split())
    #処理
    ans = max(A+B,A+C,B+C)
    #出力
    print(ans)
