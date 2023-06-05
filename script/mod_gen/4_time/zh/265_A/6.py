def problem265_a(x, y, n):
    if x >= y:
        return n * x
    else:
        return (n // 3) * y + (n % 3) * x

if __name__ == '__main__':
    problem265_a()