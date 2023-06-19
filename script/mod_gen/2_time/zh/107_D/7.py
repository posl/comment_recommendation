def findMedian(a):
    n = len(a)
    if n == 1:
        return a[0]
    elif n == 2:
        return (a[0]+a[1])/2
    else:
        a.sort()
        if n%2 == 0:
            return a[int(n/2)]
        else:
            return (a[int(n/2)]+a[int(n/2)-1])/2

if __name__ == '__main__':
    findMedian()