def check(h, w):
    for i in range(3):
        if sum(h[i]) != h[i][3]:
            return False
    for i in range(3):
        if sum(w[i]) != w[i][3]:
            return False
    return True
