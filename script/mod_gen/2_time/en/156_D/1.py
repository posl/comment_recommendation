def modpow(a, b, m):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return modpow(a * a % m, b / 2, m)
    else:
        return a * modpow(a, b - 1, m) % m

if __name__ == '__main__':
    modpow()