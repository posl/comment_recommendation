def get_max_product(n):
    max_product = 0
    n_str = str(n)
    n_len = len(n_str)
    for i in range(1, n_len):
        n1 = int(n_str[:i])
        n2 = int(n_str[i:])
        max_product = max(max_product, n1 * n2)
    return max_product

if __name__ == '__main__':
    get_max_product()