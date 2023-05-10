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
    Y = int(input())
    while True:
        Y += 1
        if Y % 4 == 2:
            print(Y)
            break

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
    # input
    Y = int(input())

    # compute

    # output
    if Y%4 == 2:
        print(Y)
    else:
        print(Y+4-Y%4+2)

=======
Suggestion 5

def main():
    Y = int(input())
    if Y % 4 == 2:
        print(Y)
    else:
        print(Y + (4 - Y % 4) + 2)

=======
Suggestion 6

def main():
    Y = int(input())
    while True:
        if Y % 4 == 2:
            print(Y)
            break
        Y += 1

=======
Suggestion 7

def main():
    y = int(input())
    while y % 4 != 2:
        y += 1
    print(y)
