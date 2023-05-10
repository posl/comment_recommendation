def calc_balls(n, a, b):
    if n <= a:
        return n
    else:
        return a + (n - a) % (a + b)
