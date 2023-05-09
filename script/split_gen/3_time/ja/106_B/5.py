def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
N = int(input())
count = 0
for i in range(1, N+1):
    if i % 2 != 0 and is_prime(i):
        count += 1
print(count)
