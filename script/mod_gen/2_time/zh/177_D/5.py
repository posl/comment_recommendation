def sum_of_products(a):
    a.sort()
    n = len(a)
    s = 0
    for i in range(n):
        s += a[i] * (n - i - 1) * (i + 1)
    return s

if __name__ == '__main__':
    sum_of_products()