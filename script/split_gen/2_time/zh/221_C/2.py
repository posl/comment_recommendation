def calc_max_product(n):
    n = str(n)
    max_product = 0
    for i in range(1, len(n)):
        left = int(n[:i])
        right = int(n[i:])
        max_product = max(max_product, left * right)
    return max_product
