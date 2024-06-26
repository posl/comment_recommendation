def count_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return len(divisors)
n = int(input())
count = 0
for i in range(1, n+1, 2):
    if count_divisors(i) == 8:
        count += 1
print(count)
