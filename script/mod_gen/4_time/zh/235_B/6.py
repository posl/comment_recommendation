def get_last_height(N, H):
    last_height = H[0]
    for i in range(N-1):
        if H[i] < H[i+1]:
            last_height = H[i+1]
    return last_height

if __name__ == '__main__':
    get_last_height()