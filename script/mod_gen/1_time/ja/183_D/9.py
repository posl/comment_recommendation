def main():
    N, W = map(int, input().split())
    # 人数, 毎分のリットル数
    # お湯を使う人の数を記録する
    water = [0] * 200001
    for i in range(N):
        S, T, P = map(int, input().split())
        # 時刻, 時刻, 毎分のリットル数
        # 時刻の区間内にお湯を使う人がいることを記録する
        water[S] += P
        water[T] -= P
    # お湯を使う人がいる区間の数を記録する
    water_sum = [0] * 200001
    water_sum[0] = water[0]
    for i in range(1, 200001):
        water_sum[i] = water_sum[i - 1] + water[i]
    for i in range(200001):
        if water_sum[i] > W:
            # お湯を使う人がいる区間の数が毎分のリットル数を超えたら
            # No
            print("No")
            return
    # Yes
    print("Yes")

if __name__ == '__main__':
    main()