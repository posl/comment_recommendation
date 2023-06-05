def median(a):
    n = len(a)
    a.sort()
    if n%2 == 0:
        return a[n//2-1]
    else:
        return a[n//2]

if __name__ == '__main__':
    median()