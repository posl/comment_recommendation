def count_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            if i%2 == 1:
                divisors += 1
            if i != n//i and (n//i)%2 == 1:
                divisors += 1
    return divisors
n = int(input())
ans = 0
for i in range(1, n+1, 2):
    if count_divisors(i) == 8:
        ans += 1
print(ans)
