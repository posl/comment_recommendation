def get_min_watering_times(n, h):
    min_watering_times = 0
    for i in range(n):
        if i == 0:
            if h[i] > 0:
                min_watering_times += h[i]
        else:
            if h[i] > h[i - 1]:
                min_watering_times += h[i] - h[i - 1]
    return min_watering_times

if __name__ == '__main__':
    get_min_watering_times()