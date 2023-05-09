def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    # 総再生時間
    total_time = sum(A)
    # T秒後の曲
    song = (T - 1) // total_time + 1
    # T秒後の曲の再生開始時刻
    start_time = total_time * (song - 1)
    # T秒後の曲の再生終了時刻
    end_time = total_time * song
    # T秒後の曲の再生終了時刻までの残り時間
    remaining_time = end_time - T
    # T秒後の曲の再生終了時刻までの残り時間を超えるまでの曲の再生時間
    for i in range(N):
        remaining_time -= A[i]
        if remaining_time < 0:
            print(i + 1, T - start_time)
            break

if __name__ == '__main__':
    main()