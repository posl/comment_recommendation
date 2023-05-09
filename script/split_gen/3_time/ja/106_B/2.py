def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
N = int(input())
count = 0
for i in range(1, N+1, 2):
    if is_prime(i):
        count += 1
print(count)
