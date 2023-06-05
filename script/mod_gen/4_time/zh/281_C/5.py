def get_next_song(song_num, song_list):
    if song_num >= len(song_list):
        return 1
    else:
        return song_num + 1

if __name__ == '__main__':
    get_next_song()