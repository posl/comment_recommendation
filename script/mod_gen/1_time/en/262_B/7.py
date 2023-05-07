def get_combination(n, r):
    if n < r:
        return 0
    if n == r:
        return 1
    return get_combination(n - 1, r) + get_combination(n - 1, r - 1)

if __name__ == '__main__':
    get_combination()