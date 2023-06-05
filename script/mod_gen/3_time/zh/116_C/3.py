def get_min_watering_times(N, h):
    left = 0
    right = 0
    count = 0
    for i in range(N):
        if h[i] == 0:
            continue
        if left == 0:
            left = i + 1
            right = i + 1
            count += h[i]
        else:
            if i + 1 == right:
                count += h[i]
            else:
                count += h[i] * (i + 1 - left)
            right = i + 1
    return count

if __name__ == '__main__':
    get_min_watering_times()