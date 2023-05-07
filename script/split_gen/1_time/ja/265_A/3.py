def main():
    #入力
    X, Y, N = map(int, input().split())
    # 処理
    ans = 0
    while N > 0:
        if N % 3 == 0:
            ans += Y * (N // 3)
            N -= N // 3 * 3
        else:
            ans += X
            N -= 1
    #出力
    print(ans)
