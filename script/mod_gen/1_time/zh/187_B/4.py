def count_slope(a, b):
    if a[0] - b[0] == 0:
        return 0
    else:
        return (a[1] - b[1]) / (a[0] - b[0])

if __name__ == '__main__':
    count_slope()