def is_prime(n):
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True
n = int(input())
c = 0
for i in range(1, n+1, 2):
    if is_prime(i):
        c += 1
print(c)
