def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
a, b, c, d = map(int, input().split())

if __name__ == '__main__':
    is_prime()