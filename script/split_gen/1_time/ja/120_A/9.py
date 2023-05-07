def main():
    #入力
    a,b,c = map(int, input().split())
    #処理
    if a*c <= b:
        ans = c
    else:
        ans = b//a
    #出力
    print(ans)
