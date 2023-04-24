Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    P = int(input())
    coins = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    count = 0
    for coin in coins:
        count += P // coin
        P %= coin
    print(count)

=======
Suggestion 2

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 3

def main():
    P = int(input())
    count = 0
    for i in range(10, 0, -1):
        count += P // math.factorial(i)
        P %= math.factorial(i)
    print(count)

=======
Suggestion 4

def main():
    P = int(input())
    coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    factorials = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    coins.reverse()
    factorials.reverse()
    count = 0
    for i in range(len(coins)):
        if P >= factorials[i]:
            count += P // factorials[i]
            P = P % factorials[i]
        if P == 0:
            break
    print(count)

=======
Suggestion 5

def main():
    P = int(input())
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[i - 2] * i)
    coins.reverse()
    ans = 0
    for coin in coins:
        ans += P // coin
        P %= coin
    print(ans)

=======
Suggestion 6

def main():
    p = int(input())
    coins = [1]
    for i in range(1, 10):
        coins.append(coins[i-1]*(i+1))
    coins.reverse()
    ans = 0
    for coin in coins:
        ans += p//coin
        p %= coin
    print(ans)

=======
Suggestion 7

def main():
    P = int(input())
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1] * i)
    coins.reverse()
    count = 0
    for coin in coins:
        count += P // coin
        P %= coin
    print(count)

=======
Suggestion 8

def main():
    p = int(input())
    coins = [1]
    for i in range(2,11):
        coins.append(coins[-1]*i)
    coins.reverse()
    count = 0
    for coin in coins:
        count += p//coin
        p %= coin
    print(count)

=======
Suggestion 9

def main():
    P = int(input())
    coins = [1]
    i = 1
    while i <= 9:
        coins.append(coins[i-1] * (i+1))
        i += 1
    i = 9
    count = 0
    while P > 0:
        if P >= coins[i]:
            P -= coins[i]
            count += 1
        else:
            i -= 1
    print(count)

=======
Suggestion 10

def main():
    p = int(input())
    coins = [1,2,3,4,5,6,7,8,9,10]
    for i in range(11,10000000):
        coins.append(coins[-1]*i)

    ans = 0
    for i in range(len(coins)-1,-1,-1):
        if p >= coins[i]:
            ans += p // coins[i]
            p = p % coins[i]
    print(ans)
