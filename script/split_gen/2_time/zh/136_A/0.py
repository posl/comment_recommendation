def pour_water(a,b,c):
    if c <= a - b:
        return 0
    else:
        return c - (a - b)
