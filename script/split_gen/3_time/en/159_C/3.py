def get_max_volume(L):
    max_volume = 0
    for i in range(1, L):
        for j in range(1, L):
            k = L - i - j
            if k < 1:
                break
            max_volume = max(max_volume, i * j * k)
    return max_volume
L = int(input())
print(get_max_volume(L))
