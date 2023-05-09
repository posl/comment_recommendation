def main():
    # 1. 入力
    n = int(input())
    a = list(map(int, input().split()))
    # 2. 計算
    # 2.1. a をソート
    a.sort()
    # 2.2. a の最大値を求める
    max_a = a[-1]
    # 2.3. a の最大値の約数を求める
    divisor = []
    for i in range(1, int(max_a**0.5)+1):
        if max_a % i == 0:
            divisor.append(i)
            if max_a // i != i:
                divisor.append(max_a // i)
    # 2.4. a の最大値の約数で割り切れる数を求める
    divisor.sort()
    for d in divisor:
        if all([ai % d == 0 for ai in a]):
            ans = d
    # 3. 出力
    print(ans)

if __name__ == '__main__':
    main()