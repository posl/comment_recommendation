def main():
    # 文字列の取得
    s = "atcoder"
    # 入力
    l, r = map(int, input().split())
    # 出力
    print(s[l-1:r])
