def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
P = int(input())
coins = [factorial(i) for i in range(1,11)][::-1]
count = 0
for coin in coins:
    while P >= coin:
        P -= coin
        count += 1
print(count)
