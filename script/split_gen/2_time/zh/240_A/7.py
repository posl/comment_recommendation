def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True
a, b, c, d = map(int, input().split())
for n in range(1, 100):
    if a <= n <= b and c <= n <= d:
        print('High') if is_prime(n) else print('Low')
        exit()
