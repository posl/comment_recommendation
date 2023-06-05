def get_median(a):
    a.sort()
    l = len(a)
    if l%2 == 1:
        return a[(l-1)//2]
    else:
        return a[l//2-1]

if __name__ == '__main__':
    get_median()