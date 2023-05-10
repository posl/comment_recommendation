def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1
p = int(input())
coins = [factorial(i) for i in range(1, 11)][::-1]
i = 0
count = 0
while p > 0:
    count += p // coins[i]
    p %= coins[i]
    i += 1
print(count)
