def get_max_platform_height(N, H):
    max_height = H[0]
    for i in range(1, N):
        if H[i] > H[i-1]:
            max_height = H[i]
    return max_height

if __name__ == '__main__':
    get_max_platform_height()