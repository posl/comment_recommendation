Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    p = int(input())
    coins = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
    count = 0
    for i in coins:
        while p >= i:
            p -= i
            count += 1
    print(count)

=======
Suggestion 2

def main():
    P = int(input())
    coins = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
    ans = 0
    for i in coins:
        if P >= i:
            ans += P // i
            P = P % i
    print(ans)

=======
Suggestion 3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 4

def main():
    P = int(input())
    coin = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
    ans = 0
    for i in coin:
        ans += P // i
        P %= i
    print(ans)

=======
Suggestion 5

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

=======
Suggestion 6

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

P = int(input())

coin = 0
for i in range(10, 0, -1):
    coin += P // factorial(i)
    P = P % factorial(i)
print(coin)

=======
Suggestion 7

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

p = int(input())
c = 0
for i in range(10, 0, -1):
    c += p // fac(i)
    p = p % fac(i)

print(c)

=======
Suggestion 8

def main():
    p = int(input())
    coin_list = [1,2,6,24,120,720,5040,40320,362880,3628800]
    count = 0
    for i in reversed(coin_list):
        if p >= i:
            count += p // i
            p = p % i
    print(count)

=======
Suggestion 9

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

P = int(input())
coin = 0
for i in range(10, 0, -1):
    if P >= fact(i):
        coin += P // fact(i)
        P = P % fact(i)
print(coin)
