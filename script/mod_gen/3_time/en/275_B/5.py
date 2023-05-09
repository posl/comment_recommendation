def modinv(a, m):
    """
    a^-1 (mod m)
    """
    b = m
    u = 1
    v = 0
    while b > 0:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    if u < 0:
        u += m
    return u

if __name__ == '__main__':
    modinv()