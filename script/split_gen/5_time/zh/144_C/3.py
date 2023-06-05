def f(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1
n = int(input())
count = 0
while n > 1:
    n = n // f(n)
    count += 1
print(count)
