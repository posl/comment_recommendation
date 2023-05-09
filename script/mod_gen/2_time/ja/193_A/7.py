def main():
    # 標準入力から数値を受け取る
    A, B = map(int, input().split())
    # 計算結果を出力する
    print((A - B) / A * 100)

if __name__ == '__main__':
    main()