def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True

if __name__ == '__main__':
    is_prime()