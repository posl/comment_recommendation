def main():
    # 文字列の入力
    S = input()
    # 出力
    print(S.count("+") - S.count("-"))

if __name__ == '__main__':
    main()