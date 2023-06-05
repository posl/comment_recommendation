def problem238_b(n, a):
    a = sorted(a)
    a.append(a[0]+360)
    max_diff = 0
    for i in range(n):
        diff = a[i+1] - a[i]
        if diff > max_diff:
            max_diff = diff
    return 360 - max_diff

if __name__ == '__main__':
    problem238_b()