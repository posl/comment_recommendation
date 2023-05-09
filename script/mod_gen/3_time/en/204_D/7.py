def oven():
    # N個の料理を作る
    N = int(input())
    # T_iはi番目の料理の焼く時間
    T = list(map(int, input().split()))
    # 一番時間がかかる料理の時間を求める
    max_time = max(T)
    # 一番時間がかかる料理の時間を除いた残りの料理の時間を求める
    T.remove(max_time)
    # 一番時間がかかる料理の時間と残りの料理の時間の合計を求める
    total_time = max_time + sum(T)
    # 一番時間がかかる料理の時間と残りの料理の時間の合計を出力する
    print(total_time)
oven()

if __name__ == '__main__':
    oven()