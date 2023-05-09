def main():
    # 標準入力から A, B を取得する
    a, b = map(int, input().split())
    # A, B の各桁の合計を求める
    a_sum = 0
    b_sum = 0
    for i in range(3):
        a_sum += a % 10
        b_sum += b % 10
        a = a // 10
        b = b // 10
    # 各桁の合計の大きい方を出力する
    if a_sum >= b_sum:
        print(a_sum)
    else:
        print(b_sum)

if __name__ == '__main__':
    main()