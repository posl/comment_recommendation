def main():
    #入力
    N, K = map(int, input().split())
    #処理
    ans = 0
    while N > 0:
        N //= K
        ans += 1
    #出力
    print(ans)
