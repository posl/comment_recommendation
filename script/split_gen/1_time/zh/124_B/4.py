def find_sea(h):
    cnt = 1
    max_h = h[0]
    for i in range(1, len(h)):
        if h[i] > max_h:
            cnt += 1
            max_h = h[i]
    return cnt
