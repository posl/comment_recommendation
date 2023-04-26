Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x == 0:
        if y == 0:
            print(0)
        elif y == 1:
            print(2)
        else:
            print(1)
    elif x == 1:
        if y == 0:
            print(1)
        elif y == 1:
            print(0)
        else:
            print(2)
    elif x == 2:
        if y == 0:
            print(2)
        elif y == 1:
            print(1)
        else:
            print(0)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x == 0 and y == 1:
        print(2)
    elif x == 0 and y == 2:
        print(0)
    elif x == 1 and y == 0:
        print(0)
    elif x == 1 and y == 2:
        print(2)
    elif x == 2 and y == 0:
        print(2)
    elif x == 2 and y == 1:
        print(0)
    elif x == y:
        print(x)

main()

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x == 0 and y == 1:
        print(2)
    elif x == 0 and y == 2:
        print(0)
    elif x == 1 and y == 0:
        print(0)
    elif x == 1 and y == 2:
        print(2)
    elif x == 2 and y == 0:
        print(2)
    elif x == 2 and y == 1:
        print(0)
    else:
        print(x)

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    elif x == 0 and y == 1:
        print(2)
    elif x == 1 and y == 2:
        print(0)
    elif x == 2 and y == 0:
        print(1)
    elif y == 0 and x == 1:
        print(2)
    elif y == 1 and x == 2:
        print(0)
    elif y == 2 and x == 0:
        print(1)

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print([0, 1, 2][x + y])

=======
Suggestion 7

def main():
    x, y = map(int, input().split())
    print((x+y+1)%3)
