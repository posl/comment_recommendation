def main():
    S = input()
    # 文字列の重複を削除
    S = list(set(S))
    # 文字列の重複を削除した結果が2つの場合
    if len(S) == 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()