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
        else:
            y += 1

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
    if y % 4 == 2:
        print(y)
    else:
        print(y + (4 - y % 4) + 2)

=======
Suggestion 5

def main():
    year = int(input())
    while True:
        if year % 4 == 2:
            break
        else:
            year += 1
    print(year)

=======
Suggestion 6

def main():
    Y = int(input())
    while True:
        Y += 1
        if Y%4 == 2:
            print(Y)
            break

=======
Suggestion 7

def main():
    y = int(input())
    while y <= 3000:
        y += 1
        if y % 4 == 2:
            print(y)
            break
    return
