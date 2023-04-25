Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    P = int(input())
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    ans = 0
    for c in coins[::-1]:
        ans += P // c
        P %= c
    print(ans)

=======
Suggestion 2

def main():
    p = int(input())
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    coins.reverse()
    count = 0
    for coin in coins:
        count += p // coin
        p = p % coin
    print(count)

=======
Suggestion 3

def main():
    P = int(input())
    coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    while P > 0:
        for i in range(10):
            if P >= coins[-1-i]:
                P = P - coins[-1-i]
                count = count + 1
                break
    print(count)

=======
Suggestion 4

def main():
    P = int(input())
    count = 0
    for i in range(10, 0, -1):
        if P >= math.factorial(i):
            count += P // math.factorial(i)
            P %= math.factorial(i)
    print(count)

=======
Suggestion 5

def main():
    p = int(input())
    coins = [10**i for i in range(1, 8)]
    coins.reverse()
    ans = 0
    for c in coins:
        ans += p // c
        p %= c
    print(ans)

=======
Suggestion 6

def main():
    P = int(input())
    coin = [1]
    for i in range(2, 11):
        coin.append(coin[-1]*i)
    ans = 0
    for c in reversed(coin):
        ans += P//c
        P %= c
    print(ans)

=======
Suggestion 7

def main():
    p = int(input())
    coins = [0] * 10
    for i in range(1, 11):
        coins[i-1] = i * (i + 1) // 2
    coins.reverse()
    ans = 0
    for i in range(10):
        ans += p // coins[i]
        p %= coins[i]
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dp = [10000000 for i in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(10):
            if i - coins[j] >= 0:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    print(dp[n])

=======
Suggestion 9

def get_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

=======
Suggestion 10

def coin(P):
    coins = []
    for i in range(1,11):
        coins.append(i)
    coins.reverse()
    count = 0
    for coin in coins:
        if P == 0:
            break
        if P >= coin:
            count += P // coin
            P = P % coin
    return count

P = int(input())
print(coin(P))
