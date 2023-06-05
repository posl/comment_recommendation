def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("length of a and b must be equal")
    product = 0
    for i in range(len(a)):
        product += a[i] * b[i]
    return product

if __name__ == '__main__':
    dot_product()