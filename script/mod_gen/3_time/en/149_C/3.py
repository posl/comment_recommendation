def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    return pow(2, x-1, x) == 1

if __name__ == '__main__':
    is_prime()