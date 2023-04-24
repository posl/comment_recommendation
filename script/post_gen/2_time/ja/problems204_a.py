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
    else:
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
    if x == 0:
        if y == 0:
            print(0)
        elif y == 1:
            print(2)
        elif y == 2:
            print(1)
    elif x == 1:
        if y == 0:
            print(1)
        elif y == 1:
            print(0)
        elif y == 2:
            print(2)
    elif x == 2:
        if y == 0:
            print(2)
        elif y == 1:
            print(1)
        elif y == 2:
            print(0)

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)

=======
Suggestion 4

def main():
    x,y = map(int,input().split())
    if (x+y) == 1:
        print(2)
    elif (x+y) == 2:
        print(0)
    else:
        print(1)

=======
Suggestion 5

def main():
    x,y = map(int,input().split())
    if x == y:
        print(x)
    else:
        print(3-x-y)

main()

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    print((x + 1) % 3)
