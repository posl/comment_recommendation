def main():
    N, K = map(int, input().split())
    if K % 2 == 0:
        # Kが偶数の場合
        # a + b ≡ b + c ≡ c + a ≡ 0 (mod K) となる組み合わせの数を数える
        # まず、a ≡ b ≡ c ≡ 0 (mod K) の場合
        ans = (N // K) ** 3
        # 次に、a ≡ c (mod K) かつ b ≡ 0 (mod K) の場合
        ans += (N // K) ** 2 * (N % K + 1)
        # 最後に、a ≡ b ≡ c (mod K) かつ a, b, c はすべて 0 でない場合
        ans += (N // K) * (N % K + 1) ** 2
    else:
        # Kが奇数の場合
        # a + b ≡ b + c ≡ c + a ≡ 0 (mod K) となる組み合わせの数を数える
        # まず、a ≡ b ≡ c ≡ 0 (mod K) の場合
        ans = (N // K) ** 3
        # 次に、a ≡ c (mod K) かつ b ≡ 0 (mod K) の場合
        ans += (N // K + 1) ** 3
        # 最後に、a ≡ b ≡ c (mod K) かつ a, b, c はすべて 0 でない場合
        ans += (N // K) * (N % K + 1) ** 2
    print(ans)

if __name__ == '__main__':
    main()