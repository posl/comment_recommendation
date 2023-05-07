def main():
    #入力
    X, Y, A, B = map(int, input().split())
    #処理
    ans = 0
    while X * A < Y and X * A - X <= B:
        X *= A
        ans += 1
    ans += (Y - X - 1) // B
    #出力
    print(ans)
