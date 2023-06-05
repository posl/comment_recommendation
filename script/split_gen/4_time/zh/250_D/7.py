def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
n = int(input())
ans = 0
for p in range(2, int(n**0.25)+1):
    if is_prime(p):
        q = 1
        while p*(q**3) <= n:
            q += 1
            if p*(q**3) <= n:
                ans += 1
print(ans)
