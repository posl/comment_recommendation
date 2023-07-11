def findMedian(a,b,c):
    if a>b:
        if b>c:
            return b
        elif a>c:
            return c
        else:
            return a
    else:
