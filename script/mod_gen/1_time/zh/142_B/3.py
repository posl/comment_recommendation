def count_roller_coaster(N, K, h):
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    return count

if __name__ == '__main__':
    count_roller_coaster()