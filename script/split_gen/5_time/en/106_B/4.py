def divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
n = int(input())
count = 0
for i in range(1, n + 1, 2):
    if len(divisors(i)) == 8:
        count += 1
print(count)
