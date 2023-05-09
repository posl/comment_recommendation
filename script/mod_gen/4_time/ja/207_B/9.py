def calc_operation_count(a, b, c, d):
    if a < b:
        return -1
    if c >= d * b:
        return 0
    return ((d * b - a) + (c - b) - 1) // (c - b)

if __name__ == '__main__':
    calc_operation_count()