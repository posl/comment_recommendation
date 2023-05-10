def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
a, b, c, d = map(int, input().split())
for i in range(100):
    if is_prime(a + i):
        break
for j in range(100):
    if is_prime(c + j):
        break
