def get_minimum_cost(x, y, n):
    if x == y:
        return x * n
    if n % 3 == 0:
        return n / 3 * y
    elif n % 3 == 1:
        return (n / 3 + 1) * y
    else:
        return (n / 3 + 1) * y
