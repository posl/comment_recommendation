def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    # プレイリストの長さ
    playlist_len = sum(A)
    # T秒後に流れている曲の番号
    song_num = T // playlist_len
    # T秒後に流れている曲が流れ始めてから何秒か
    song_time = T % playlist_len
    # T秒後に流れている曲が流れ始めてから何秒かを計算
    for i in range(N):
        if song_time >= A[i]:
            song_time -= A[i]
        else:
            print(i+1, song_time)
            break
