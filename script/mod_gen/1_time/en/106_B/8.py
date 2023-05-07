def get_divisors(n):
    return [x for x in range(1, n + 1) if n % x == 0]

if __name__ == '__main__':
    get_divisors()