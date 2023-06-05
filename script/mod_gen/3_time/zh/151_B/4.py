def func(n, k, m, a):
    if n * m - sum(a) > k:
        return -1
    else:
        return max(0, n * m - sum(a))

if __name__ == '__main__':
    func()