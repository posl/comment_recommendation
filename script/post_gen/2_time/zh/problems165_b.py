Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    year = 0
    money = 100
    while money < x:
        money += money // 100
        year += 1
    print(year)

=======
Suggestion 2

def getYear(x):
    year = 0
    sum = 100
    while sum < x:
        sum = sum + int(sum * 0.01)
        year += 1
    return year

=======
Suggestion 3

def problem165_b():
    x = int(input())
    y = 100
    year = 0
    while y < x:
        y = int(y * 1.01)
        year = year + 1
    print(year)

problem165_b()

=======
Suggestion 4

def main():
    x = int(input())
    money = 100
    year = 0
    while money < x:
        money = int(money * 1.01)
        year += 1
    print(year)

=======
Suggestion 5

def main():
    x = int(input())
    money = 100
    years = 0
    while money < x:
        money = int(money * 1.01)
        years += 1

    print(years)

=======
Suggestion 6

def main():
    x = int(input())
    y = 100
    i = 0
    while y < x:
        i += 1
        y += y // 100
    print(i)

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
    balance = 100
    year = 0
    while balance < x:
        balance = balance + balance // 100
        year += 1
    print(year)

=======
Suggestion 9

def main():
    x = int(input())
    money = 100
    year = 0
    while money < x:
        year += 1
        money = money * 1.01 // 1
    print(year)

=======
Suggestion 10

def problem165_b():
    x = int(input())
    balance = 100
    year = 0
    while balance < x:
        year += 1
        balance = int(balance * 1.01)
    print(year)
