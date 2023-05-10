Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    a = x // 500
    b = x % 500 // 5
    print(a * 1000 + b * 5)

=======
Suggestion 2

def main():
    X = int(input())
    print(int((X // 500) * 1000 + ((X % 500) // 5) * 5))

=======
Suggestion 3

def main():
    X = int(input())
    print(((X//500)*1000) + (((X%500)//5)*5))

=======
Suggestion 4

def solve(x):
    return (x // 500) * 1000 + ((x % 500) // 5) * 5

=======
Suggestion 5

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(amount + 1):
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]

x = int(input())
coins = [1, 5, 10, 50, 100, 500]
amount = 1000 - x
print(coin_change(coins, amount))

=======
Suggestion 6

def main():
    x = int(input())
    print((x//500)*1000+((x%500)//5)*5)

=======
Suggestion 7

def main():
    x = int(input())
    count = 0
    count += x // 500 * 1000
    x = x % 500
    count += x // 5 * 5
    print(count)

=======
Suggestion 8

def change(x):
    return x//500*1000 + (x%500)//5*5

=======
Suggestion 9

def main():
    x = int(input())
    coin = [500, 100, 50, 10, 5, 1]
    ans = 0
    for i in range(6):
        ans += (x // coin[i]) * (coin[i] // 5) * 5
        x = x % coin[i]
    print(ans)

=======
Suggestion 10

def exchange(x):
    # 500円玉
    a = x // 500
    x -= a * 500
    # 100円玉
    b = x // 100
    x -= b * 100
    # 50円玉
    c = x // 50
    x -= c * 50
    # 10円玉
    d = x // 10
    x -= d * 10
    # 5円玉
    e = x // 5
    x -= e * 5
    # 1円玉
    f = x // 1
    x -= f * 1
    return 1000 * a + 5 * e
