Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        y += 1

=======
Suggestion 2

def main():
    Y = int(input())
    while True:
        if Y % 4 == 2:
            print(Y)
            break
        Y += 1

=======
Suggestion 3

def main():
    Y = int(input())
    if Y % 4 == 2:
        print(Y)
    else:
        print(Y + (4 - Y % 4))

=======
Suggestion 4

def main():
    y = int(input())
    while y % 4 != 2:
        y += 1
    print(y)

=======
Suggestion 5

def main():
    Y = int(input())
    while Y % 4 != 2:
        Y += 1
    print(Y)

=======
Suggestion 6

def main():
    y = int(input())
    if y % 4 == 2:
        print(y)
    else:
        print(y + 2)

=======
Suggestion 7

def main():
    Y = int(input())
    print(Y + (4 - Y % 4))

=======
Suggestion 8

def main():
    Y = int(input())
    print((Y+2)//4*4)
