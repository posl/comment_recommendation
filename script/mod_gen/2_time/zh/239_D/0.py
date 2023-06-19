def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for x in range(3, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True
a, b, c, d = map(int, input().split())

if __name__ == '__main__':
    is_prime()