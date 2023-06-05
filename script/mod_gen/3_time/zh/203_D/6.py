def get_median(a):
    a.sort()
    b = int(len(a)/2)
    if len(a)%2 == 0:
        return (a[b-1]+a[b])/2
    else:
        return a[b]

if __name__ == '__main__':
    get_median()