def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for m in range(3, int(n**0.5)+1, 2):
        if n%m == 0:
            return False
    return True

if __name__ == '__main__':
    is_prime()