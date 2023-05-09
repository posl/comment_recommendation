Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    y = 100
    year = 0
    while y < x:
        y = int(y * 1.01)
        year += 1
    print(year)

=======
Suggestion 2

def main():
    x = int(input())
    y = 100
    count = 0
    while y < x:
        y = int(y * 1.01)
        count += 1
    print(count)

=======
Suggestion 3

def main():
    x = int(input())
    year = 0
    balance = 100
    while balance < x:
        year += 1
        balance = int(balance * 1.01)
    print(year)

=======
Suggestion 4

def main():
    X = int(input())
    Y = 100
    count = 0
    while Y < X:
        Y = int(Y * 1.01)
        count += 1
    print(count)

=======
Suggestion 5

def problem165_b(x):
    balance = 100
    year = 0
    while balance < x:
        balance = int(balance * 1.01)
        year += 1
    return year

=======
Suggestion 6

def main():
    x = int(input())
    balance = 100
    year = 0
    while balance < x:
        balance = balance + (balance // 100)
        year += 1
    print(year)

=======
Suggestion 7

def main():
    x = int(input())
    y = 100
    year = 0
    while y < x:
        y = y * 1.01
        year += 1
    print(year)

=======
Suggestion 8

def compute():
    x = int(input())
    y = 100
    count = 0
    while y < x:
        y = int(y * 1.01)
        count += 1
    return count

print(compute())

=======
Suggestion 9

def interest():
    x = int(input())
    balance = 100
    year = 0
    while balance < x:
        balance = int(balance * 1.01)
        year += 1
    print(year)

interest()

=======
Suggestion 10

def main():
    x = int(input())
    result = 0
    deposit = 100
    while deposit < x:
        deposit += deposit // 100
        result += 1
    print(result)
