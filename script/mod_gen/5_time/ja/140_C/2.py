def get_max_sum(n, b):
    a = [0] * (n + 1)
    a[0] = b[0]
    a[1] = b[0]
    for i in range(1, n - 1):
        a[i + 1] = min(b[i], b[i - 1])
    a[n] = b[n - 2]
    return sum(a)

if __name__ == '__main__':
    get_max_sum()