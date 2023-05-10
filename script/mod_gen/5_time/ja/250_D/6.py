def is_prime(n):
    if n == 1: return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0: return False
    return True
N = int(input())
ans = 0
for p in range(2, int(N**0.25)+1):
    if is_prime(p):
        q = 1
        while p * q**3 <= N:
            ans += 1
            q += 1
print(ans)

if __name__ == '__main__':
    is_prime()