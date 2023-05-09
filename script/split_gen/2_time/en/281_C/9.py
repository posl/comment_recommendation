def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    # 1. 総再生時間を求める
    total_time = 0
    for i in range(N):
        total_time += A[i]
    # 2. Tを総再生時間で割った余りを求める
    T = T % total_time
    # 3. 余りを再生時間の合計から引く
    for i in range(N):
        T -= A[i]
        # 4. 余りがマイナスになったら、その時の曲番号を出力する
        if T < 0:
            print(i + 1, A[i] + T)
            break
