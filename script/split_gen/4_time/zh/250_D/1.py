def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
n = int(input())
ans = 0
for i in range(1, int(n**0.25)+1):
    if n%i == 0:
        if is_prime(i):
            for j in range(1, int((n/i)**(1/3))+1):
                if (n/i)%j == 0:
                    if is_prime(j) and is_prime((n/i)/j):
                        ans += 1
print(ans)
