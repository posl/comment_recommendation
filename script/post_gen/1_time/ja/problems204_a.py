Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
    elif x == 0 and y == 2:
        print(1)
    elif x == 1 and y == 0:
        print(2)
    elif x == 2 and y == 1:
        print(0)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    elif x == 0 and y == 1:
        print(2)
    elif x == 1 and y == 0:
        print(2)
    elif x == 1 and y == 2:
        print(0)
    elif x == 2 and y == 1:
        print(0)
    elif x == 2 and y == 0:
        print(1)
    elif x == 0 and y == 2:
        print(1)

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    elif x == 0 and y == 1 or x == 1 and y == 2 or x == 2 and y == 0:
        print(2)
    else:
        print(0)

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)

main()

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
    print((x + 1) % 3) if x != y else print(x)

=======
Suggestion 7

def main():
    x, y = map(int, input().split())
    print(3 - (x + y))
