Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

=======
Suggestion 2

def main():
    P = int(input())
    #P = 10000000
    #P = 119
    #P = 9

    # 10! = 3628800
    # 9! = 362880
    # 8! = 40320
    # 7! = 5040
    # 6! = 720
    # 5! = 120
    # 4! = 24
    # 3! = 6
    # 2! = 2
    # 1! = 1

    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # 1, 1, 1, 1, 1, 1, 1, 1, 1, 1

    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # 1, 1, 1, 1, 1, 1, 1, 1, 1, 1

    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # 1, 1, 1, 1, 1, 1, 1, 1, 1, 1

    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # 1, 1, 1, 1, 1, 1, 1, 1, 1, 1

    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # 1, 1, 1, 1, 1, 1, 1, 1, 1, 1

    # 1, 2, 3, 4, 5, 6, 7

=======
Suggestion 3

def get_min_coin_num(P):
    coin_num = 0
    for i in range(10,0,-1):
        coin_num += P // factorial(i)
        P %= factorial(i)
    return coin_num

=======
Suggestion 4

def main():
    p = int(input())
    n = 10
    a = [1]
    for i in range(1, n):
        a.append(a[i-1] * (i+1))
    c = 0
    for i in range(n-1, -1, -1):
        c += p // a[i]
        p %= a[i]
    print(c)

=======
Suggestion 5

def main():
    print("请输入一个整数：")
    n = int(input())
    if n < 0 or n > 10 ** 7:
        print("输入的数不在范围内")
        return
    print("需要的最少硬币数为：")
    print(coin(n))

=======
Suggestion 6

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 7

def count_coins(p):
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1]*i)
    count = 0
    for i in range(9, -1, -1):
        count += p // coins[i]
        p %= coins[i]
    return count

while True:
    try:
        p = int(input())
        print(count_coins(p))
    except:
        break

=======
Suggestion 8

def exchange_coin(p):
    coin = [1,2,6,24,120,720,5040,40320,362880,3628800]
    count = 0
    for i in range(9,-1,-1):
        while p >= coin[i]:
            p -= coin[i]
            count += 1
    return count

=======
Suggestion 9

def main():
    P = int(input())
    coins = [1]
    for i in range(1,11):
        coins.append(coins[i-1]*(i+1))
    count = 0
    for i in range(10,0,-1):
        count += P//coins[i]
        P = P%coins[i]
    print(count)
