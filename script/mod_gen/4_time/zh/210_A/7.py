def calc_cost(n, a, x, y):
    if n <= a:
        return n * x
    else:
        return a * x + (n - a) * y

if __name__ == '__main__':
    calc_cost()