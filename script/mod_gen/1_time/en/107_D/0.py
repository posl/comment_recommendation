def median(a):
    a.sort()
    n = len(a)
    if n % 2 == 0:
        return (a[n // 2 - 1] + a[n // 2]) / 2
    else:
        return a[n // 2]

if __name__ == '__main__':
    median()