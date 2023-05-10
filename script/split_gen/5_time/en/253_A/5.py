def is_median(a,b,c):
    if a <= b <= c or c <= b <= a:
        return True
    else:
        return False
