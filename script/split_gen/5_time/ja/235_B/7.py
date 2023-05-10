def get_max_hight(N, H):
    max_hight = 0
    for i in range(N):
        if max_hight < H[i]:
            max_hight = H[i]
    return max_hight
