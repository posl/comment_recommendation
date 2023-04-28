Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    count = 0
    while x >= 500:
        x -= 500
        count += 1000
    while x >= 5:
        x -= 5
        count += 5
    print(count)

=======
Suggestion 2

def main():
    x = int(input())
    print((x // 500) * 1000 + ((x % 500) // 5) * 5)

=======
Suggestion 3

def main():
    x = int(input())
    res = 0
    res += (x // 500) * 1000
    x -= (x // 500) * 500
    res += (x // 5) * 5
    print(res)

=======
Suggestion 4

def exchange(x):
    coins = [500, 100, 50, 10, 5, 1]
    count = 0
    for coin in coins:
        count += x // coin
        x %= coin
    return count

print(exchange(int(input())) * 1000)

=======
Suggestion 5

def solve():
    X = int(input())
    y = 0
    y += (X // 500) * 1000
    X = X % 500
    y += (X // 5) * 5
    print(y)

=======
Suggestion 6

def solve():
    X = int(input())
    ans = 0
    ans += (X//500)*1000
    X = X%500
    ans += (X//5)*5
    print(ans)

=======
Suggestion 7

def exchange(x):
    if x >= 500:
        return 1000
    elif x >= 5:
        return 5
    elif x >= 1:
        return 1
    else:
        return 0

x = int(input())
r = 0
while x > 0:
    r += exchange(x)
    x -= exchange(x)
print(r)

=======
Suggestion 8

def solve():
    x = int(input())
    print((x//500)*1000+((x%500)//5)*5)

=======
Suggestion 9

def exchange(x):
    # 500円玉
    fivehundred = x // 500
    # 100円玉
    onehundred = (x - fivehundred * 500) // 100
    # 50円玉
    fifty = (x - fivehundred * 500 - onehundred * 100) // 50
    # 10円玉
    ten = (x - fivehundred * 500 - onehundred * 100 - fifty * 50) // 10
    # 5円玉
    five = (x - fivehundred * 500 - onehundred * 100 - fifty * 50 - ten * 10) // 5
    # 1円玉
    one = x - fivehundred * 500 - onehundred * 100 - fifty * 50 - ten * 10 - five * 5
    return fivehundred * 1000 + onehundred * 100 + fifty * 10 + five * 2

x = int(input())
print(exchange(x))

=======
Suggestion 10

def get_max_joy(money):
    joy = 0
    coins = [500,100,50,10,5,1]
    for coin in coins:
        joy += money // coin
        money = money % coin
    return joy
