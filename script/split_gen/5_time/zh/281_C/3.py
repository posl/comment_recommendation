def get_next_song(song):
    global song_list
    global song_time
    global song_now
    global song_time_now
    song_now += 1
    if song_now == len(song_list):
        song_now = 0
    song_time_now = song_time[song_now]
    return song_list[song_now]
