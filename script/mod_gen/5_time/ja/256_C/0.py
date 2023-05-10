def check(h, w):
    for i in range(3):
        if sum(h[i]) != h[i][0] * 3:
            return False
    for i in range(3):
        if sum(w[i]) != w[i][0] * 3:
            return False
    return True

if __name__ == '__main__':
    check()