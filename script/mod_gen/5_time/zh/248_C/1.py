def f(n, m, k):
    if k < n or k > n * m:
        return 0
    elif n == 1:
        return 1
    else:
        return sum([f(n - 1, m, k - i) for i in range(1, m + 1)])

if __name__ == '__main__':
    f()