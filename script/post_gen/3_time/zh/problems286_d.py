Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def pay(x, coins):
    if x == 0:
        return True
    if len(coins) == 0:
        return False
    for i in range(coins[0][1]+1):
        if pay(x - coins[0][0] * i, coins[1:]):
            return True
    return False

=======
Suggestion 2

def pay(money, coin, num):
    if money == 0:
        return True
    if money < 0:
        return False
    if num <= 0 and money >= 1:
        return False
    return pay(money, coin, num-1) or pay(money-coin[num-1], coin, num)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum > X:
        print('No')
    else:
        print('Yes')

=======
Suggestion 4

def pay_coin(coins, money):
    if money == 0:
        return True
    if money < 0 or len(coins) == 0:
        return False
    return pay_coin(coins[1:], money - coins[0]) or pay_coin(coins[1:], money)

=======
Suggestion 5

def get_input():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    return n, x, a, b

=======
Suggestion 6

def isPayable(coinList, value):
    if value == 0:
        return True
    elif len(coinList) == 0:
        return False
    else:
        for i in range(0, coinList[0][1]+1):
            if value >= i*coinList[0][0]:
                if isPayable(coinList[1:], value - i*coinList[0][0]):
                    return True
        return False

=======
Suggestion 7

def solve():
    N, X = map(int, input().split())
    for i in range(N):
        A, B = map(int, input().split())
        X -= A * B
    if X >= 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def get_input():
    N,X = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    return N,X,A,B

=======
Suggestion 9

def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum >= X:
        print("Yes")
    else:
        print("No")
