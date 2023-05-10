def solve():
    # === 数値を取得 ===
    s = input()
    t = input()
    # === 処理 ===
    if s == t[0:len(s)]:
        print('Yes')
    else:
        print('No')
