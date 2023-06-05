def get_max_f(x, n, s, w):
    f = 0
    for i in range(n):
        if s[i] == '0' and w[i] < x:
            f += 1
        elif s[i] == '1' and w[i] >= x:
            f += 1
    return f

if __name__ == '__main__':
    get_max_f()