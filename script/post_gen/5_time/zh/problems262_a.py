Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def next_sport_year(year):
    while True:
        year += 1
        if year % 4 == 2:
            return year

=======
Suggestion 2

def main():
    Y = int(input())
    while Y < 2000 or Y > 3000:
        Y = int(input())
    while Y % 4 != 2:
        Y += 1
    print(Y)

=======
Suggestion 3

def main():
    Y = int(input())
    while Y < 2000 or Y > 3000:
        print('输入的年份不在范围内，请重新输入！')
        Y = int(input())
    while Y % 4 != 2:
        Y += 1
    print(Y)

=======
Suggestion 4

def problems262_a():
    y = int(input())
    print(y+2-(y%4))

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
        y += 1
        if y % 4 == 2:
            break
    print(y)
main()

=======
Suggestion 7

def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        else:
            y += 1

=======
Suggestion 8

def main():
    Y = int(input())
    while Y < 2000 or Y > 3000:
        Y = int(input())
    while (Y % 4) != 2:
        Y += 1
    print(Y)

=======
Suggestion 9

def main():
    year = int(input())
    while True:
        if year % 4 == 2:
            print(year)
            break
        year += 1
