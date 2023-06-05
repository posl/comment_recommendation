def find_median(alist):
    alist.sort()
    n = len(alist)
    if n % 2 == 0:
        return alist[n//2 - 1]
    else:
        return alist[n//2]

if __name__ == '__main__':
    find_median()