Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    p = int(input())
    coin = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    ans = 0
    for i in range(9, -1, -1):
        ans += p // coin[i]
        p %= coin[i]
    print(ans)

=======
Suggestion 2

def main():
    p = int(input())
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    coins.reverse()
    cnt = 0
    for c in coins:
        cnt += p // c
        p %= c
    print(cnt)

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
    coins = [1,2,6,24,120,720,5040,40320,362880,3628800]
    cnt = 0
    for i in range(10):
        cnt += P//coins[9-i]
        P = P%coins[9-i]
    print(cnt)

=======
Suggestion 5

def main():
    P = int(input())
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1] * i)
    ans = 0
    for i in range(10, 0, -1):
        ans += P // coins[i-1]
        P %= coins[i-1]
    print(ans)

=======
Suggestion 6

def main():
    P = int(input())
    coin = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ans = 0
    for c in coin:
        if P >= factorial(c):
            ans += P // factorial(c)
            P = P % factorial(c)
    print(ans)

=======
Suggestion 7

def main():
    P = int(input())
    # 硬貨の種類
    coin = [1,2,6,24,120,720,5040,40320,362880,3628800]
    coin.reverse()
    ans = 0
    for i in range(len(coin)):
        if P >= coin[i]:
            ans += P // coin[i]
            P = P % coin[i]
    print(ans)

=======
Suggestion 8

def main():
    p = int(input())
    coins = [1]
    for i in range(1, 11):
        coins.append(coins[-1] * (i+1))
    coins.reverse()
    ans = 0
    for coin in coins:
        ans += p // coin
        p %= coin
    print(ans)

=======
Suggestion 9

def main():
    P = int(input())
    # 10! から 1! までの硬貨をリストに格納
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1] * i)
    #print(coins)
    ans = 0
    # 10! から 1! までの硬貨を使って、支払うことができる枚数を求める
    for i in range(10, 0, -1):
        ans += P // coins[i-1]
        P %= coins[i-1]
    print(ans)

=======
Suggestion 10

def main():
    # 入力
    P = int(input())
