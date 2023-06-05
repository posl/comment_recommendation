def get_max_height(N, H):
    max_height = 0
    for i in range(N):
        if H[i] > max_height:
            max_height = H[i]
    return max_height
