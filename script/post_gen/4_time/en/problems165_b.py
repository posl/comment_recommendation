Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    balance = 100
    years = 0
    while balance < x:
        balance = int(balance * 1.01)
        years += 1
    print(years)

=======
Suggestion 2

def main():
    x = int(input())
    balance = 100
    year = 0
    while balance < x:
        year += 1
        balance = int(balance * 1.01)
    print(year)

=======
Suggestion 3

def main():
    x = int(input())
    y = 100
    cnt = 0
    while y < x:
        y = int(y * 1.01)
        cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    x = int(input())
    balance = 100
    year = 0

    while balance < x:
        balance = int(balance * 1.01)
        year += 1

    print(year)

=======
Suggestion 5

def main():
    x = int(input())
    balance = 100
    years = 0
    while balance < x:
        years += 1
        balance = int(balance * 1.01)
    print(years)

=======
Suggestion 6

def main():
    x = int(input())
    deposit = 100
    year = 0
    while deposit < x:
        deposit = int(deposit * 1.01)
        year += 1
    print(year)

=======
Suggestion 7

def main():
    x = int(input())
    year = 0
    balance = 100

    while balance < x:
        year += 1
        balance = int(balance * 1.01)

    print(year)

=======
Suggestion 8

def main():
    # input
    x = int(input())
    # compute
    year = 0
    balance = 100
    while balance < x:
        year += 1
        balance = int(balance * 1.01)
    # output
    print(year)

=======
Suggestion 9

def main():
    x = int(input())
    balance = 100
    years = 0
    while(balance < x):
        balance += int(balance/100)
        years += 1
    print(years)
