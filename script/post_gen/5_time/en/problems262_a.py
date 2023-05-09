Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    y = int(input())
    while True:
        y += 1
        if y % 4 == 2:
            print(y)
            break

=======
Suggestion 2

def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        y += 1

=======
Suggestion 3

def main():
    y = int(input())
    while (y % 4 != 2):
        y += 1
    print(y)

=======
Suggestion 4

def main():
    year = int(input())
    while year % 4 != 2:
        year += 1
    print(year)

=======
Suggestion 5

def main():
    Y = int(input())
    while (Y % 4 != 2):
        Y += 1
    print(Y)

=======
Suggestion 6

def main():
    Y = int(input())
    if Y%4 == 0:
        print(Y+2)
    else:
        print(Y+4-Y%4)

=======
Suggestion 7

def main():
    year = int(input())
    while (year % 4) != 2:
        year += 1
    print(year)
    return

=======
Suggestion 8

def main():
    Y = int(input())
    print(Y + 2 - (Y % 4))
