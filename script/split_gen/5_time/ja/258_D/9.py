def calc_time(n, x, stage):
    time = 0
    for i in range(n):
        if x == 0:
            break
        if x - stage[i][0] >= 0:
            time += stage[i][0] + stage[i][1]
            x -= stage[i][0]
        else:
            time += x + stage[i][1]
            x = 0
    return time
