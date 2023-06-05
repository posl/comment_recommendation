def max_product(n):
    n_str = str(n)
    n_len = len(n_str)
    max_product = 0
    for i in range(1,n_len):
        a = int(n_str[:i])
        b = int(n_str[i:])
        product = a*b
        if product > max_product:
            max_product = product
    return max_product
