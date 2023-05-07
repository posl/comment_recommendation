def calc_song(N, T, A):
    song = 0
    time = 0
    for i in range(N):
        if time + A[i] > T:
            break
        time += A[i]
        song = i + 1
    time = T - time
    return song, time
