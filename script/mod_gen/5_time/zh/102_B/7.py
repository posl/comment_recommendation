def max_abs_diff(n, a):
    max_diff = 0
    for i in range(n):
        for j in range(i+1, n):
            diff = abs(a[i] - a[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

if __name__ == '__main__':
    max_abs_diff()