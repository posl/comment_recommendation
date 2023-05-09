def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
n = int(input())
count = 0
for i in range(1, n+1):
    if i % 2 == 1 and len(divisors(i)) == 8:
        count += 1
print(count)
