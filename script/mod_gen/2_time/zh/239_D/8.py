def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1, 2):
        if n % i

if __name__ == '__main__':
    is_prime()