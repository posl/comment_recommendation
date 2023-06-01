Synthesizing 10/10 solutions

=======
Suggestion 1

def problem165_b(x):
    balance = 100
    year = 0
    while balance < x:
        balance = int(balance * 1.01)
        year += 1
    return year

=======
Suggestion 2

def main():
    x = int(input())
    i = 0
    a = 100
    while a < x:
        a = int(a * 1.01)
        i += 1
    print(i)

=======
Suggestion 3

def main():
    x = int(input())
    y = 100
    count = 0
    while y < x:
        y += y//100
        count += 1
    print(count)

=======
Suggestion 4

def main():
    x = int(input())
    balance = 100
    year = 0
    while True:
        year += 1
        balance = int(balance * 1.01)
        if balance >= x:
            break
    print(year)

=======
Suggestion 5

def main():
    X = int(input())
    balance = 100
    year = 0
    while balance < X:
        balance = int(balance * 1.01)
        year += 1
    print(year)

=======
Suggestion 6

def main():
    x = int(input())
    year = 0
    money = 100
    while money < x:
        money = int(money * 1.01)
        year += 1
    print(year)

=======
Suggestion 7

def main():
    X = int(input())
    deposit = 100
    year = 0
    while deposit < X:
        deposit = int(deposit * 1.01)
        year += 1
    print(year)

=======
Suggestion 8

def main():
    x = int(input())
    balance = 100
    year = 0
    while balance < x:
        balance = int(balance * 1.01)
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
        money += money // 100
    print(year)

=======
Suggestion 10

def main():
    x = int(input())
    m = 100
    year = 0
    while m < x:
        m = int(m * 1.01)
        year += 1
    print(year)
