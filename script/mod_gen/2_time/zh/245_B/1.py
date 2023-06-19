def find_missing_number(n, a):
    a.sort()
    if a[0] != 0:
        return 0
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            return a[i - 1] + 1
    return a[n - 1] + 1

if __name__ == '__main__':
    find_missing_number()