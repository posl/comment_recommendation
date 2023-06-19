def maxProduct(a,b,c,d):
    if b < c or d < a:
        return -1
    else:
        return max(a*c, a*d, b*c, b*d)
