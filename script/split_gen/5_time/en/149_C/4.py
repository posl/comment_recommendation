def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True
x = int(input())
while is_prime(x) == False:
    x += 1
print(x)
