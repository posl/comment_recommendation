def dice(a,b,c):
    if (a >= 1 and a <= 6) and (b >= 1 and b <= 6) and (c >= 1 and c <= 6):
        return (7 - a) + (7 - b) + (7 - c)
    else:
        return False
