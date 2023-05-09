def main():
    # 標準入力から値を取得する
    a, b, c = map(int, input().split())
    # a, b, cが全て等しいかどうか判定する
    if a == b and b == c:
        # 全て等しい場合はNoを出力する
        print('No')
    else:
        # 全て等しくない場合はYesを出力する
        print('Yes')

if __name__ == '__main__':
    main()