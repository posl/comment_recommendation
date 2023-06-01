Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    Y = int(input())
    while True:
        if Y % 4 == 2:
            print(Y)
            break
        else:
            Y = Y + 1

=======
Suggestion 2

def main():
    y = int(input())
    while y <= 3000:
        if y % 4 == 2:
            print(y)
            break
        else:
            y = y + 1

=======
Suggestion 3

def main():
    Y = int(input())
    while Y <= 3000:
        Y += 1
        if Y % 4 == 2:
            break
    print(Y)

=======
Suggestion 4

def main():
    Y = int(input())
    print(Y + 2 - Y % 4)

=======
Suggestion 5

def main():
    Y = int(input())
    while True:
        Y += 1
        if Y % 4 == 2:
            print(Y)
            break

=======
Suggestion 6

def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        y += 1

=======
Suggestion 7

def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            break
        y += 1
    print(y)

=======
Suggestion 8

def main():
    year = int(input())
    while year < 2000 or year > 3000:
        year = int(input())
    while year % 4 != 2:
        year += 1
    print(year)
main()

=======
Suggestion 9

def main():
    year = int(input())
    while True:
        if year % 4 == 2:
            print(year)
            break
        else:
            year += 1
