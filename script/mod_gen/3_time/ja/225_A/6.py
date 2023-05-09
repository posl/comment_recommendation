def main():
    # 入力
    S = input()
    # 処理
    # 文字列をソート
    S = sorted(S)
    # 文字列を結合
    S = ''.join(S)
    # 出力
    print(S)

if __name__ == '__main__':
    main()