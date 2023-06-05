def get_max_product(n):
    n = str(n)
    len_n = len(n)
    max_product = 0
    for i in range(1, len_n):
        a = int(n[0:i])
        b = int(n[i:len_n])
        product = a * b
        if product > max_product:
            max_product = product
    return max_product

if __name__ == '__main__':
    get_max_product()