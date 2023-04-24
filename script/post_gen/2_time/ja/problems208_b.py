Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    P = int(input())
    coins = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
    ans = 0
    for i in range(31, -1, -1):
        ans += P // coins[i]
        P = P % coins[i]
    print(ans)

=======
Suggestion 2

def main():
    P = int(input())
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    count = 0
    for i in range(9, -1, -1):
        if P >= coins[i]:
            count += P // coins[i]
            P = P % coins[i]
    print(count)

=======
Suggestion 3

def main():
    P = int(input())
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    coins.reverse()
    count = 0
    for coin in coins:
        if P >= coin:
            count += P // coin
            P %= coin
    print(count)

=======
Suggestion 4

def main():
    P = int(input())
    coin = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    coin.reverse()
    ans = 0
    for i in range(10):
        ans += P // coin[i]
        P %= coin[i]
    print(ans)

=======
Suggestion 5

def main():
    p = int(input())
    ans = 0
    for i in range(10,0,-1):
        ans += p // math.factorial(i)
        p %= math.factorial(i)
    print(ans)

=======
Suggestion 6

def main():
    P = int(input())
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[i-2] * i)
    coins.reverse()
    ans = 0
    for coin in coins:
        ans += P // coin
        P %= coin
    print(ans)

=======
Suggestion 7

def main():
    P = int(input())
    coin = [1]
    for i in range(1, 10):
        coin.append(coin[i-1] * (i+1))
    ans = 0
    for i in range(9, -1, -1):
        ans += P // coin[i]
        P = P % coin[i]
    print(ans)

=======
Suggestion 8

def main():
    P = int(input())
    coins = [1]
    for i in range(1, 11):
        coins.append(coins[i-1] * i)
    coins.reverse()

    ans = 0
    for coin in coins:
        ans += P // coin
        P %= coin
    print(ans)

=======
Suggestion 9

def main():
    P = int(input())
    coins = [0] * 10
    for i in range(10):
        coins[i] = factorial(i+1)
    coins.reverse()
    ans = 0
    for c in coins:
        ans += P // c
        P %= c
    print(ans)

=======
Suggestion 10

def main():
    P = int(input())
    N = 10
    A = [0] * N
    for i in range(N):
        A[N - 1 - i] = P // math.factorial(N - 1 - i)
        P -= A[N - 1 - i] * math.factorial(N - 1 - i)
    print(sum(A))
