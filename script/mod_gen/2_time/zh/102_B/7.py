def max_abs_diff(a):
    a.sort()
    return a[-1] - a[0]

if __name__ == '__main__':
    max_abs_diff()