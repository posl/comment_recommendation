def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n & 1 == 0: return False
 
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
 
    return True
n = int(input())
ans = 0
for i in range(1, int(n**(1/3)) + 1):
    if is_prime(i):
        tmp = n // i
        if tmp**(1/3) == int(tmp**(1/3)):
            ans += 1
print(ans)

if __name__ == '__main__':
    is_prime()