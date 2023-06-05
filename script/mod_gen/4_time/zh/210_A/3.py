def calc_cost(n, a, x, y):
    cost = 0
    if n <= a:
        cost = n * x
    else:
        cost = a * x + (n - a) * y
    return cost

if __name__ == '__main__':
    calc_cost()