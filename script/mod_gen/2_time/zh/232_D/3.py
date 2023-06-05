def check(n, m, a, b, c, d, p):
    for i in range(m):
        if ((p[a[i]-1] < p[b[i]-1]) != (c[i]-1 < d[i]-1)):
            return False
    return True

if __name__ == '__main__':
    check()