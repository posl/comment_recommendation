def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 ==0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True
a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    if is_prime(i):
        break
else:
    print('No')
    exit()
for i in range(c, d+1):
    if is_prime(i):
        break
else:
    print('No')
    exit()
print('Yes')
