def is_prime(n):
    if n == 1:
        return False
    for p in range(2, n):
        if n % p == 0:
            return False
    ret

if __name__ == '__main__':
    is_prime()