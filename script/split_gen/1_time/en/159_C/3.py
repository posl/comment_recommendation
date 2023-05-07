def find_max_volume(L):
    max_volume = 0
    for i in range(1, L):
        for j in range(1, L - i):
            k = L - i - j
            volume = i * j * k
            if volume > max_volume:
                max_volume = volume
    return max_volume
