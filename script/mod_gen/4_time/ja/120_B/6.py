def main():
    # 標準入力から A, B, K を取得する
    a, b, k = map(int, input().split())
    # A, B を割り切る正整数の集合を計算する
    divisors = set()
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            divisors.add(i)
    # divisors を昇順にソートして、K 番目の要素を出力する
    divisors = sorted(divisors)
    print(divisors[k - 1])

if __name__ == '__main__':
    main()