def calc_balls(n, a, b):
    if n <= a:
        return n
    else:
        return a + (n - a) % (a + b)

if __name__ == '__main__':
    calc_balls()