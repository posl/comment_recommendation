def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True
n = int(input())
p = []
for k in range(1, int(n**0.25)+1):
    if n % k == 0:
        p.append(k)
        p.append(n//k)
ans = 0
for k in p:
    if is_prime(k):
        if n % k == 0:
            if is_prime(n//k):
                ans += 1
print(ans)

if __name__ == '__main__':
    is_prime()