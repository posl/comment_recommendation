def max_absolute_difference(n, a):
    a.sort()
    return a[-1] - a[0]

if __name__ == '__main__':
    max_absolute_difference()