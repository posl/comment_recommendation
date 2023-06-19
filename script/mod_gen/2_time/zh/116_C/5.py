def water_flower(N, h):
    count = 0
    while True:
        l = 0
        r = 0
        for i in range(N):
            if h[i] != 0:
                l = i
                break
        for i in range(N-1, -1, -1):
            if h[i] != 0:
                r = i
                break
        if l == r:
            count += h[l]
            break
        count += max(h[l:r+1])
        for i in range(l, r+1):
            h[i] -= max(h[l:r+1])
    return count

if __name__ == '__main__':
    water_flower()