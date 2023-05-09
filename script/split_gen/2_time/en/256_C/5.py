def check(h, w):
    if h[0] == w[0] + w[1] + w[2] and h[1] == w[0] + w[1] + w[2] and h[2] == w[0] + w[1] + w[2]:
        if w[0] == h[0] + h[1] + h[2] and w[1] == h[0] + h[1] + h[2] and w[2] == h[0] + h[1] + h[2]:
            return True
    return False
