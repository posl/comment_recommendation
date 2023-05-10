def get_min_operations(N, h):
    count = 0
    for i in range(N):
        if i == 0:
            count += h[i]
        else:
            count += max(h[i] - h[i-1], 0)
    return count
