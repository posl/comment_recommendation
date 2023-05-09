def main():
    n, w = map(int, input().split())
    # 1分間にどれだけの水が使われているかを記録する
    water = [0] * (200000 + 1)
    for i in range(n):
        s, t, p = map(int, input().split())
        water[s] += p
        water[t] -= p
    # 1分間にどれだけの水が使われているかを累積和で求める
    for i in range(1, 200000 + 1):
        water[i] += water[i - 1]
    # 1分間にどれだけの水が使われているかを確認する
    for i in range(1, 200000 + 1):
        if water[i] > w:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()