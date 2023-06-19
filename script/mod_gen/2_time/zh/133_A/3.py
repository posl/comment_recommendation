def get_min_cost(n, a, b):
    if n*a < b:
        return n*a
    else:
        return b

if __name__ == '__main__':
    get_min_cost()