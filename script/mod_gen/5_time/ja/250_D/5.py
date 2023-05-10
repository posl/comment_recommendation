def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True
n = int(input())
ans = 0
for p in range(2, int(n**(1/4))+1):
    if is_prime(p):
        if n % p == 0:
            q = n // p
            if q**(1/3) == int(q**(1/3)):
                ans += 1
print(ans)

if __name__ == '__main__':
    is_prime()