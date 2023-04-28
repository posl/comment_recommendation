Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    year = int(input())
    while True:
        year += 1
        if year % 4 == 2:
            print(year)
            break

=======
Suggestion 2

def main():
    Y = int(input())
    while True:
        if Y % 4 == 2:
            print(Y)
            break
        else:
            Y += 1

=======
Suggestion 3

def main():
    year = int(input())
    while True:
        if year % 4 == 2:
            print(year)
            break
        else:
            year += 1

=======
Suggestion 4

def main():
    Y = int(input())
    Y += 2
    if Y % 4 == 0:
        print(Y)
    else:
        while Y % 4 != 0:
            Y += 1
        print(Y)

=======
Suggestion 5

def main():
    year = int(input())
    while (year % 4) != 2:
        year += 1
    print(year)

=======
Suggestion 6

def main():
    Y = int(input())
    while Y % 4 != 2:
        Y += 1
    print(Y)

=======
Suggestion 7

def main():
    Y = int(input())
    while (Y % 4) != 2:
        Y += 1
    print(Y)

=======
Suggestion 8

def main():
    y = int(input())
    print(y + 2 - y % 4)

=======
Suggestion 9

def get_next_year(year):
    while True:
        if year % 4 == 2:
            return year
        year += 1

=======
Suggestion 10

def main():
    Y = int(input())
    print(Y+2-Y%4)
