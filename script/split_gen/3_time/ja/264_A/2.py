def main():
    # 文字列の入力
    s = input()
    # 整数の入力
    l, r = map(int, input().split())
    # 出力
    print(s[l-1:r])
