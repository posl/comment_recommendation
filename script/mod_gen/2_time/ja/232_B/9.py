def solve():
    # === 入力 ===
    # S
    S = input()
    # T
    T = input()
    # === 処理 ===
    # S と T の長さは等しい
    # S の長さと T の長さは等しい
    # なので、S の長さでループさせる
    for i in range(len(S)):
        # S の i 番目の文字
        s = S[i]
        # T の i 番目の文字
        t = T[i]
        # S の i 番目の文字と T の i 番目の文字が異なる場合
        if s != t:
            # No を出力して終了
            print("No")
            return
    # S と T が一致する場合
    # Yes を出力
    print("Yes")

if __name__ == '__main__':
    solve()