def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(pow(n, 0.5)) + 1, 2):
        if n % i == 0:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    for i in range(2, int(pow(n, 1 / 3)) + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            print(i, n // i)
            break
