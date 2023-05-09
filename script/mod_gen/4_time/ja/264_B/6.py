def main():
    # 標準入力から R, C を取得する
    R, C = map(int, input().split())
    # R, C について、black と white を出力する
    if R % 2 == 0:
        if C % 2 == 0:
            print('white')
        else:
            print('black')
    else:
        if C % 2 == 0:
            print('black')
        else:
            print('white')

if __name__ == '__main__':
    main()