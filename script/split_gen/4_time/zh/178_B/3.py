def max_product(a,b,c,d):
    max = a * c
    if a * d > max:
        max = a * d
    if b * c > max:
        max = b * c
    if b * d > max:
        max = b * d
    return max
