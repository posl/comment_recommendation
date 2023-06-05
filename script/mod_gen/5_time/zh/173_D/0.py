def get_max_comfort(n, a):
    c = [0 for i in range(n)]
    c[0] = a[0]
    for i in range(1, n):
        c[i] = min(c[i-1], a[i])
    s = sum(a)
    for i in range(1, n):
        s += min(a[i-1], a[i])
    return s - max(c)

if __name__ == '__main__':
    get_max_comfort()