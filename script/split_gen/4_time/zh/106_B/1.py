def divisors(n):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1
    return count
n = int(input())
count = 0
for i in range(1, n+1):
    if i%2 == 1 and divisors(i) == 8:
        count += 1
print(count)
