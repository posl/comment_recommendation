def problem265_a(x, y, n):
    if x == y:
        return x * n
    elif x > y:
        return y * n
    else:
        return x * n + (n // 3) * (y - x)

if __name__ == '__main__':
    problem265_a()