def powmod(x, n, mod):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return powmod(x * x % mod, n // 2, mod)
    else:
        return x * powmod(x, n - 1, mod) % mod

if __name__ == '__main__':
    powmod()