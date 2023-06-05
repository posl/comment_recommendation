def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    # 重复播放的时间
    loop = sum(a)
    # 重复播放的次数
    times = t // loop
    # 剩余时间
    rest = t % loop
    # 重复播放的次数内，播放的歌曲
    song = 0
    # 重复播放的次数内，播放的歌曲的时间
    song_time = 0
    for i in range(n):
        song_time += a[i]
        if song_time > rest:
            song = i + 1
            break
    # 剩余时间内，播放的歌曲
    song += times * n
    print(song, song_time)
