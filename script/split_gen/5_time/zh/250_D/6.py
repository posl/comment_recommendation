def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    if n == 1:
        return False
    else:
        return True
n = int(input())
count = 0
for i in range(1, int(n ** 0.25) + 1):
    if n % i == 0:
        if is_prime(i):
            if i ** 3 <= n:
                if is_prime(n // i):
                    count += 1
print(count)
