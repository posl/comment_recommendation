def get_bit_and(a, b):
    c = 0
    while a > 0 and b > 0:
        if a % 2 == 1 and b % 2 == 1:
            c += 1
        a /= 2
        b /= 2
    return c
