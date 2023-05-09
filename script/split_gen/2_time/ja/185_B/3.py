def main():
    N, M, T = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 時刻 0 から T までのバッテリー残量を記録するリスト
    battery = [0] * (T + 1)
    # 時刻 0 から T までのバッテリー残量を計算する
    for i in range(M):
        # 時刻 0 からカフェに到着するまでのバッテリー残量を計算する
        for j in range(A[i]):
            if battery[j] < N:
                battery[j + 1] = battery[j] + 1
            else:
                battery[j + 1] = battery[j]
        # カフェに到着してからカフェを出発するまでのバッテリー残量を計算する
        for j in range(A[i], B[i]):
            if battery[j] > 0:
                battery[j + 1] = battery[j] - 1
            else:
                battery[j + 1] = battery[j]
        # カフェを出発してから帰宅するまでのバッテリー残量を計算する
        for j in range(B[i], T + 1):
            if battery[j] < N:
                battery[j + 1] = battery[j] + 1
            else:
                battery[j + 1] = battery[j]
    # 帰宅時のバッテリー残量が 0 でなければ Yes を出力する
    if battery[T] > 0:
        print("Yes")
    # 帰宅時のバッテリー残量が 0 であれば No を出力する
    else:
        print("No")
