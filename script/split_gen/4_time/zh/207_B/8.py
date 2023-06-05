def solve(a,b,c,d):
    if a<=b*c:
        return -1
    else:
        for i in range(1,a):
            if a<=i*b:
                return i
        return -1
