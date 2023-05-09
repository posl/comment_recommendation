Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    p = int(input())
    coins = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
    count = 0
    for c in coins:
        while p >= c:
            p -= c
            count += 1
    print(count)

=======
Suggestion 2

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 3

def main():
    p = int(input())
    coin = [1,2,6,24,120,720,5040,40320,362880,3628800]
    count = 0
    for i in range(9,-1,-1):
        if coin[i] <= p:
            count += p // coin[i]
            p = p % coin[i]
    print(count)

=======
Suggestion 4

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

=======
Suggestion 5

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

P = int(input())

count = 0
for i in range(10, 0, -1):
    count += P // factorial(i)
    P = P % factorial(i)

print(count)

=======
Suggestion 6

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

P = int(input())

coins = [factorial(n) for n in range(1,11)][::-1]

count = 0
for coin in coins:
    while P >= coin:
        P -= coin
        count += 1

print(count)

=======
Suggestion 7

def get_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * get_factorial(n-1)

=======
Suggestion 8

def factorial(x):
    if x == 0: return 1
    else: return x * factorial(x-1)
