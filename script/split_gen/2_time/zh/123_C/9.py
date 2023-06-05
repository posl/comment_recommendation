def get_min_time(a, b, c, d, e):
    time = [a, b, c, d, e]
    min_time = 0
    for i in range(5):
        if time[i] % 10 != 0:
            time[i] = time[i] + 10 - time[i] % 10
    min_time = max(time)
    return min_time
