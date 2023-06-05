def problem257_a(n, x):
    if n < 1 or n > 100 or x < 1 or x > n * 26:
        return None
    else:
        return chr(x % 26 + 64)

if __name__ == '__main__':
    problem257_a()