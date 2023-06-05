def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
n = int(input())
count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    divisors = get_divisors(i)
    if len(divisors) == 8:
        count += 1
print(count)
