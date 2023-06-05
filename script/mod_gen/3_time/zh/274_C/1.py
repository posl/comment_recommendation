def get_distance(n, a):
    a.insert(0, 0)
    b = [0] * (2 * n + 1)
    for i in range(1, n + 1):
        b[i] = 1
    for i in range(1, n):
        b[a[i]] += b[i]
        b[a[i] + 1] += b[i]
    b[2 * n] += b[n]
    for i in range(n + 1, 2 * n):
        b[a[i]] += b[i]
        b[a[i] + 1] += b[i]
    return b

if __name__ == '__main__':
    get_distance()