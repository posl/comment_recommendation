def calc_time(n, t, k, a):
    time = [0 for i in range(n)]
    for i in range(n):
        if k[i] == 0:
            time[i] = t[i]
        else:
            max_time = 0
            for j in range(k[i]):
                if time[a[i][j] - 1] > max_time:
                    max_time = time[a[i][j] - 1]
            time[i] = max_time + t[i]
    return max(time)
