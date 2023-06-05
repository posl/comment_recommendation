def dot_product(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])

if __name__ == '__main__':
    dot_product()