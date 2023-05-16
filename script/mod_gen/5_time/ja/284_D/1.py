def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if not n % i:
            return False
        i += 1
    return True

if __name__ == '__main__':
    is_prime()