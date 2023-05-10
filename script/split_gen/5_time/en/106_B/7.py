def divisors(n):
    return [x for x in range(1, n+1) if n % x == 0]
n = int(input())
count = 0
for i in range(1, n+1, 2):
    if len(divisors(i)) == 8:
        count += 1
print(count)
