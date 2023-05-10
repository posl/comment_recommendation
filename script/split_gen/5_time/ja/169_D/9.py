def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False
    return True
n = int(input())
ans = 0
for i in range(2, int(n**0.5)+1):
    if is_prime(i) and n%i == 0:
        while n%i == 0:
            n //= i
            ans += 1
