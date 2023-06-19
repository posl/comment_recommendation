def get_max_product(n):
    n_str = str(n)
    n_len = len(n_str)
    if n_len == 2:
        return n
    elif n_len == 3:
        return int(n_str[0]) * int(n_str[1:])
    else:
        max_product = 0
        for i in range(1, n_len - 1):
            product = int(n_str[0:i]) * int(n_str[i:])
            if product > max_product:
                max_product = product
        return max_product

if __name__ == '__main__':
    get_max_product()