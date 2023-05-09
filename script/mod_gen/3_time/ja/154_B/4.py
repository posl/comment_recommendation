def main():
    # 文字列Sを入力
    S = input()
    # 文字列Sの長さを取得
    length = len(S)
    # 文字列Sの長さ分ループ
    for i in range(0, length):
        # 文字列Sの長さ分xを出力
        print("x", end = "")

if __name__ == '__main__':
    main()