def check(n, a, b, x):
    for i in range(n):
        if a[i] <= x <= b[i] or b[i] <= x <= a[i]:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    check()