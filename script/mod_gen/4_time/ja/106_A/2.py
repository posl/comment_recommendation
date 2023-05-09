def main():
    # 標準入力から A と B を取得する
    A, B = map(int, input().split())
    # 道を除いた畑の面積を計算して出力する
    print(A*B-(A+B-1))

if __name__ == '__main__':
    main()