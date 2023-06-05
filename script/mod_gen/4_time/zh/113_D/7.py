def calculate(h,w,k):
    if k == 1:
        return 1
    if k == w:
        return 1
    if k == w-1:
        return w-1
    if k == 2:
        return w
    if k == w-2:
        return w*(w-1)/2
    if k == 3:
        return w*(w-1)/2
    if k == w-3:
        return w*(w-1)*(w-2)/6
    if k == 4:
        return w*(w-1)*(w-2)/6
    if k == w-4:
        return w*(w-1)*(w-2)*(w-3)/24
    if k == 5:
        return w*(w-1)*(w-2)*(w-3)/24
    if k == w-5:
        return w*(w-1)*(w-2)*(w-3)*(w-4)/120
    if k == 6:
        return w*(w-1)*(w-2)*(w-3)*(w-4)/120
    if k == w-6:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)/720
    if k == 7:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)/720
    if k == w-7:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)*(w-6)/5040
    if k == 8:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)*(w-6)/5040
    if k == w-8:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)*(w-6)*(w-7)/40320
    if k == 9:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)*(w-6)*(w-7)/40320
    if k == w-9:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-

if __name__ == '__main__':
    calculate()