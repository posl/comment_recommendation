Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = int(input())
    deposit = 100
    year = 0
    while deposit < X:
        deposit = int(deposit * 1.01)
        year += 1
    print(year)

=======
Suggestion 2

def main():
    X = int(input())
    balance = 100
    year = 0
    while balance < X:
        balance += int(balance * 0.01)
        year += 1
    print(year)

=======
Suggestion 3

def main():
    X = int(input())
    ans = 0
    bal = 100
    while bal < X:
        bal = int(bal * 1.01)
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    x = int(input())
    y = 100
    n = 0
    while y < x:
        y = int(y * 1.01)
        n += 1
    print(n)

=======
Suggestion 5

def main():
    X = int(input())
    balance = 100
    years = 0
    while (balance < X):
        balance = int(balance * 1.01)
        years += 1
    print(years)

=======
Suggestion 6

def main():
    x = int(input())
    y = 100
    count = 0
    while y < x:
        y = int(y*1.01)
        count += 1
    print(count)

=======
Suggestion 7

def main():
    X = int(input())
    year = 0
    money = 100
    while money < X:
        money = money * 1.01
        year += 1
    print(year)

=======
Suggestion 8

def main():
    x = int(input())
    years = 0
    balance = 100
    while balance < x:
        balance = balance * 1.01
        years += 1
    print(years)

=======
Suggestion 9

def main():
    x = int(input())
    count = 0
    while x > 100:
        x = int(x * 1.01)
        count += 1
    print(count)

=======
Suggestion 10

def main():
    X = int(input())
    ans = 0
    i = 100
    while i < X:
        i = i + i // 100
        ans += 1
    print(ans)

main()
