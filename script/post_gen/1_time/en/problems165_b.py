Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = int(input())
    balance = 100
    year = 0
    while balance < X:
        balance = int(balance * 1.01)
        year += 1
    print(year)

=======
Suggestion 2

def main():
    X = int(input())
    years = 0
    balance = 100
    while balance < X:
        balance = int(balance * 1.01)
        years += 1
    print(years)

=======
Suggestion 3

def main():
    x = int(input())
    y = 100
    count = 0
    while y < x:
        y = int(y * 1.01)
        count += 1
    print(count)

=======
Suggestion 4

def main():
    X = int(input())
    balance = 100
    years = 0
    while balance < X:
        balance += balance // 100
        years += 1
    print(years)

=======
Suggestion 5

def main():
    X = int(input())
    ans = 0
    bal = 100
    while bal < X:
        bal = int(bal * 1.01)
        ans += 1
    print(ans)

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
    y = 100
    i = 0
    while y < X:
        y = int(y * 1.01)
        i += 1
    print(i)

=======
Suggestion 8

def main():
    X = int(input())
    ans = 0
    bal = 100
    while bal < X:
        ans += 1
        bal = int(bal * 1.01)
    print(ans)

=======
Suggestion 9

def main():
    x = int(input())
    year = 0
    balance = 100
    while balance < x:
        balance = balance * 101 // 100
        year += 1
    print(year)

=======
Suggestion 10

def main():
    X = int(input())
    print(X // 100)
