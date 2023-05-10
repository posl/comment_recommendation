def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
n = int(input())
l = prime_factors(n)
l = list(set(l))
l.sort()
#print(l)
ans = 0
for i in l:
    num = 0
    while n % i == 0:
        n = n // i
        num += 1
    #print(num)
    for j in range(1, num+1):
        num -= j
        if num >= 0:
            ans += 1
        else:
            break
print(ans)
