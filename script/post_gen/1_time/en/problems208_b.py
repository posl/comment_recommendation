Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 2

def solve():
    p = int(input())
    coins = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
    ans = 0
    for i in range(10):
        ans += p // coins[i]
        p %= coins[i]
    print(ans)
solve()

=======
Suggestion 3

def main():
    P = int(input())
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    ans = 0

    for i in range(9, -1, -1):
        ans += P // coins[i]
        P %= coins[i]

    print(ans)

=======
Suggestion 4

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

p = int(input())

coin = 0
for i in range(10,0,-1):
    coin += p // factorial(i)
    p %= factorial(i)
print(coin)

=======
Suggestion 5

def main():
    import sys
    import math
    input = sys.stdin.readline
    n = int(input())
    ans = 0
    for i in range(10, 0, -1):
        ans += n//math.factorial(i)
        n %= math.factorial(i)
    print(ans)

=======
Suggestion 6

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

=======
Suggestion 7

def factorial(n):
    return n * factorial(n-1) if n > 1 else 1
