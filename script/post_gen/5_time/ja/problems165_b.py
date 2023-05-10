Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    money = 100
    year = 0
    while money < x:
        money += money // 100
        year += 1
    print(year)

=======
Suggestion 2

def main():
    X = int(input())
    money = 100
    year = 0
    while money < X:
        year += 1
        money += money // 100
    print(year)

=======
Suggestion 3

def main():
    x = int(input())
    ans = 0
    money = 100
    while money < x:
        ans += 1
        money = int(money * 1.01)
    print(ans)

=======
Suggestion 4

def calc_year(x):
    year = 0
    while x > 100:
        x = x * 101 // 100
        year += 1
    return year

=======
Suggestion 5

def solve():
    x = int(input())
    y = 100
    cnt = 0
    while y < x:
        y = int(y * 1.01)
        cnt += 1
    print(cnt)

=======
Suggestion 6

def calc_year(x):
    year = 0
    money = 100
    while money < x:
        money = int(money * 1.01)
        year += 1
    return year

=======
Suggestion 7

def main():
    x = int(input())
    year = 0
    money = 100
    while money < x:
        money = int(money * 1.01)
        year += 1
    print(year)

=======
Suggestion 8

def main():
    x = int(input())
    n = 100
    count = 0
    while n < x:
        n = n + n // 100
        count = count + 1
    print(count)

=======
Suggestion 9

def main():
    x = int(input())
    y = 100
    i = 0
    while x > y:
        y = y + int(y * 0.01)
        i += 1
    print(i)

=======
Suggestion 10

def calc_year(x):
    year = 0
    balance = 100
    while balance < x:
        balance = balance + int(balance * 0.01)
        year += 1
    return year
