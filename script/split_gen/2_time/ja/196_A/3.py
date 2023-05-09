def main():
    #入力
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    #処理
    ans = max(a - d, b - c)
    #出力
    print(ans)
