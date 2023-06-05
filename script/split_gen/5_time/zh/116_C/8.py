def get_min_watering_times(N, h):
    water_times = 0
    for i in range(N):
        if h[i] == 0:
            continue
        elif h[i] == 1:
            water_times += 1
        else:
            water_times += h[i]
    return water_times
