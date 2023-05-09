def calc_diff(n, w):
    diff = 10000
    for i in range(1, n):
        s1 = sum(w[0:i])
        s2 = sum(w[i:n])
        if diff > abs(s1 - s2):
            diff = abs(s1 - s2)
    return diff

if __name__ == '__main__':
    calc_diff()