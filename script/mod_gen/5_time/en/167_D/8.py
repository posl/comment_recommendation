def teleporter(a, k):
    n = len(a)
    b = [None] * n
    b[0] = 0
    for i in range(1, n):
        b[i] = a[b[i - 1] - 1]
        if b[i] == 0:
            return a[k % i]
    return b[-1]

if __name__ == '__main__':
    teleporter()