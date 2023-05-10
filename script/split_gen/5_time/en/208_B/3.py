def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input())
count = 0
for i in range(10, 0, -1):
    if n >= factorial(i):
        count += n // factorial(i)
        n = n % factorial(i)
print(count)
