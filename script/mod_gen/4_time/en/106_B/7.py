def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

if __name__ == '__main__':
    is_prime()