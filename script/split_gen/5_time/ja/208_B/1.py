def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
p = int(input())
coins = []
for i in range(1,11):
    coins.append(factorial(i))
coins.reverse()
count = 0
for coin in coins:
    while p >= coin:
        p -= coin
        count += 1
print(count)
