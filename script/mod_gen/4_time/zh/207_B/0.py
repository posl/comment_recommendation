def get_min_operation_count(a, b, c, d):
    if a <= b * d:
        return -1
    else:
        return (c * a - b * d - 1) // (b * (c - d)) + 1

if __name__ == '__main__':
    get_min_operation_count()