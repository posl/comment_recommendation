def find_median(a):
    a.sort()
    n = len(a)
    if n % 2 == 1:
        return a[(n-1)/2]
    else:
        return a[n/2]

if __name__ == '__main__':
    find_median()