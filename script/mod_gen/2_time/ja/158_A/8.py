def main():
    # 標準入力から文字列を取得
    s = input()
    # s[0]とs[1]の文字が同じかどうか
    if s[0] == s[1]:
        # s[1]とs[2]の文字が同じかどうか
        if s[1] == s[2]:
            # s[0]とs[1]とs[2]の文字が全て同じなのでNoを出力
            print('No')
        else:
            # s[0]とs[1]の文字が同じで、s[1]とs[2]の文字が違うなのでYesを出力
            print('Yes')
    else:
        # s[0]とs[1]の文字が違うかつ、s[1]とs[2]の文字が同じなのでYesを出力
        print('Yes')

if __name__ == '__main__':
    main()