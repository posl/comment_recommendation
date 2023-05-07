def main():
    # 文字列の取得
    S = input()
    # 文字列の長さを取得
    length = len(S)
    # 回文にするために必要なハグの最小回数
    min_hug = 0
    # 文字列の長さの半分を取得
    half_length = length // 2
    # 文字列の長さが奇数の場合
    if length % 2 != 0:
        # 文字列の長さの半分の文字列を取得
        half_string = S[:half_length]
        # 文字列の長さの半分の文字列を反転
        reverse_half_string = half_string[::-1]
        # 文字列の長さの半分の文字列と反転した文字列を比較
        for i in range(half_length):
            if half_string[i] != reverse_half_string[i]:
                min_hug += 1
        # 文字列の長さの半分の文字列の後ろに文字列の長さの半分の文字列を連結
        reverse_half_string = half_string + reverse_half_string
        # 文字列の長さの半分の文字列と反転した文字列を比較
        for i in range(length):
            if S[i] != reverse_half_string[i]:
                min_hug += 1
    # 文字列の長さが偶数の場合
    else:
        # 文字列の長さの半分の文字列を取得
        half_string = S[:half_length]
        # 文字列の長さの半分の文字列を反転
        reverse_half_string = half_string[::-1]
        # 文字列の長さの半分の文字列と反転した文字列を比較
        for i in range(half_length):
            if half_string[i] != reverse_half_string[i]:
                min_hug += 1
    # 回文にするために必要なハグ

if __name__ == '__main__':
    main()