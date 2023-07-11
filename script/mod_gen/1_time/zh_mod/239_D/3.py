def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    re

if __name__ == '__main__':
    is_prime()