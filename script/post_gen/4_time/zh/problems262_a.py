Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solution():
    Y = int(input())
    while True:
        Y += 1
        if Y % 4 == 2:
            break
    print(Y)

=======
Suggestion 2

def sports(y):
    if y % 4 == 2:
        print(y)
    else:
        print(y + (2 - y % 4))

=======
Suggestion 3

def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        y += 1

=======
Suggestion 4

def main():
    y = int(input())
    while True:
        y += 1
        if y % 4 == 2:
            print(y)
            break

=======
Suggestion 5

def main():
    Y = int(input())
    while True:
        if Y % 4 == 2:
            print(Y)
            break
        else:
            Y += 1

=======
Suggestion 6

def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        else:
            y += 1

=======
Suggestion 7

def main():
    y = int(input())
    while y < 2000 or y > 3000:
        y = int(input())
    while y % 4 != 2:
        y += 1
    print(y)

=======
Suggestion 8

def main():
    year = int(input())
    while True:
        if year % 4 == 2:
            print(year)
            break
        year += 1
