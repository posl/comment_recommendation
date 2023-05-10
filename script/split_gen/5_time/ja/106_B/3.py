def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5)+1, 2):
        if n % i == 0: return False
    return True
N = int(input())
count = 0
for i in range(1, N+1, 2):
    d = 0
    for j in range(1, N+1):
        if i % j == 0:
            d += 1
    if d == 8:
        count += 1
print(count)
