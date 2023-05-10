def watering(h):
    n = len(h)
    count = 0
    for i in range(n-1):
        if h[i] < h[i+1]:
            count += h[i+1] - h[i]
    return count
