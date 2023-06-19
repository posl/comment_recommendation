def get_min_cost(n, a, b):
    if n*a < b:
        return n*a
    else:
        return b
