def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
import math
p = int(input())
coins = []
for i in range(10, 0, -1):
    coins.append(factorial(i))
count = 0
while p > 0:
    for coin in coins:
        if coin <= p:
            count += math.floor(p / coin)
            p -= math.floor(p / coin) * coin
            break
print(count)
