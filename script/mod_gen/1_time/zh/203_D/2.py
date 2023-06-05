def get_median(a):
    a.sort()
    return a[len(a) // 2]

if __name__ == '__main__':
    get_median()