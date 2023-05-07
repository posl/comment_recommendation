def main():
    N, W = map(int, input().split())
    # 時刻ごとにお湯を使う量を記録する
    water = [0] * 200001
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    # 時刻ごとにお湯を使う量を累積和で求める
    for i in range(1, 200001):
        water[i] += water[i - 1]
    # 時刻ごとにお湯を使う量が給湯器の出力量を超えていたらNo
    for i in range(200001):
        if water[i] > W:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()