def get_median(a, k):
    a.sort()
    return a[k*k//2]

if __name__ == '__main__':
    get_median()