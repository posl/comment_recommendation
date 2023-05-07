def main():
    #入力
    P, Q, R = map(int, input().split())
    #処理
    ans = min(P + Q, Q + R, R + P)
    #出力
    print(ans)
