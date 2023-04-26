Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    P = int(input())
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    ans = 0
    for i in range(9, -1, -1):
        ans += P // coins[i]
        P %= coins[i]
    print(ans)

=======
Suggestion 2

def main():
    P = int(input())
    coin = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51, 1, 2, 1, 14, 1, 2, 2, 14, 1, 6, 1, 4, 2, 2, 1, 52, 2, 5, 1, 5, 1, 15, 2, 13, 2, 2, 1, 13, 1, 2, 4, 267, 1, 4, 1, 5, 1, 4, 1, 50, 1, 2, 3, 4, 1, 6, 1, 52, 15, 2, 1, 15, 1, 2, 1, 12, 1, 10, 1, 4, 2]
    count = 0
    for i in range(10, 0, -1):
        while P >= coin[i]:
            P -= coin[i]
            count += 1
    print(count)

=======
Suggestion 3

def main():
    P = int(input())
    ans = 0
    for i in range(10, 0, -1):
        ans += P // math.factorial(i)
        P %= math.factorial(i)
    print(ans)

=======
Suggestion 4

def main():
    p = int(input())
    coins = [1]
    for i in range(2,11):
        coins.append(coins[i-2]*i)
    coins.reverse()
    ans = 0
    for coin in coins:
        ans += p // coin
        p %= coin
    print(ans)

=======
Suggestion 5

def main():
    P = int(input())
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1]*i)
    ans = 0
    for i in range(len(coins)-1, -1, -1):
        ans += P//coins[i]
        P %= coins[i]
    print(ans)

=======
Suggestion 6

def main():
    P = int(input())
    coin = [1]
    for i in range(2, 11):
        coin.append(coin[-1] * i)
    ans = 0
    for i in range(10, 0, -1):
        ans += P // coin[i - 1]
        P %= coin[i - 1]
    print(ans)

=======
Suggestion 7

def main():
    P = int(input())
    A = [1]
    for i in range(1, 11):
        A.append(A[i - 1] * i)
    A.reverse()
    ans = 0
    for i in range(10):
        ans += P // A[i]
        P %= A[i]
    print(ans)

main()

=======
Suggestion 8

def main():
    p = int(input())
    coin = [1]
    for i in range(2, 11):
        coin.append(coin[i-2]*i)
    coin.reverse()
    ans = 0
    for c in coin:
        ans += p//c
        p %= c
    print(ans)
