def main():
    # 文字列を取得
    s = input()
    # 文字列の3文字目と4文字目が等しく、5文字目と6文字目も等しいか判定
    if s[2] == s[3] and s[4] == s[5]:
        print("Yes")
    else:
        print("No")
