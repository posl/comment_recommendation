def is_prime(n):
    if n == 2:
        return True
    if n < 2 or not n % 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if not n % i:
            return False
    return True

if __name__ == '__main__':
    is_prime()