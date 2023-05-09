def getDivisors(n):
    divisors = 0
    for i in range(1,n+1):
        if n % i == 0:
            divisors += 1
    return divisors
n = int(input())
count = 0
for i in range(1,n+1):
    if i % 2 != 0:
        if getDivisors(i) == 8:
            count += 1
print(count)
