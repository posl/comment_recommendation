def main():
    N, M, T = map(int, input().split())
    cafe = [list(map(int, input().split())) for i in range(M)]
    # 滞在時間のリスト
    stay_time = []
    for i in range(M):
        stay_time.append(cafe[i][1] - cafe[i][0])
    # 滞在時間の合計
    sum_stay_time = sum(stay_time)
    # 滞在時間の合計が帰宅時刻よりも大きい場合はNo
    if sum_stay_time > T:
        print("No")
        return
    # 滞在時間の合計が帰宅時刻よりも小さい場合はYes
    if sum_stay_time < T:
        print("Yes")
        return
    # 滞在時間の合計が帰宅時刻と等しい場合は、最後に滞在したカフェの終了時刻が帰宅時刻と等しいかどうかで判定
    if sum_stay_time == T:
        if cafe[-1][1] == T:
            print("Yes")
            return
        else:
            print("No")
            return
