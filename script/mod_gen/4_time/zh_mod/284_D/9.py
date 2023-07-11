def func(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return 1, n

if __name__ == '__main__':
    func()