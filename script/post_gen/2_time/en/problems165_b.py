Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = int(input())
    years = 0
    balance = 100
    while balance < X:
        balance = int(balance * 1.01)
        years += 1
    print(years)

=======
Suggestion 2

def main():
    X = int(input())
    money = 100
    years = 0
    while money < X:
        money = int(money * 1.01)
        years += 1
    print(years)

=======
Suggestion 3

def main():
    x = int(input())
    y = 100
    year = 0
    while y < x:
        y = int(y * 1.01)
        year += 1
    print(year)

=======
Suggestion 4

def main():
    X = int(input())
    count = 0
    balance = 100
    while balance < X:
        balance = int(balance * 1.01)
        count += 1
    print(count)

=======
Suggestion 5

def main():
    X = int(input())
    year = 0
    balance = 100
    while balance < X:
        year += 1
        balance = int(balance * 1.01)
    print(year)

=======
Suggestion 6

def main():
    X = int(input())
    Y = 100
    count = 0
    while Y < X:
        Y = int(Y * 1.01)
        count += 1
    print(count)

=======
Suggestion 7

def main():
    X = int(input())
    year = 0
    balance = 100
    while balance < X:
        balance = balance * 101 // 100
        year += 1
    print(year)

=======
Suggestion 8

def main():
    X = int(input())
    year = 0
    balance = 100
    while balance < X:
        balance += (balance // 100)
        year += 1
    print(year)
