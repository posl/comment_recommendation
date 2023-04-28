Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - (x + y))

=======
Suggestion 3

def rock_paper_scissors(x,y):
    if x == y:
        print(x)
    elif x == 0 and y == 1:
        print(0)
    elif x == 0 and y == 2:
        print(2)
    elif x == 1 and y == 0:
        print(2)
    elif x == 1 and y == 2:
        print(1)
    elif x == 2 and y == 0:
        print(0)
    elif x == 2 and y == 1:
        print(1)

=======
Suggestion 4

def hand(x, y):
    if x == y:
        return x
    elif x == 0 and y == 1:
        return x
    elif x == 1 and y == 0:
        return y
    elif x == 0 and y == 2:
        return y
    elif x == 2 and y == 0:
        return x
    elif x == 1 and y == 2:
        return x
    elif x == 2 and y == 1:
        return y

x, y = input().split()

print(hand(x, y))

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    z = 0
    if x == y:
        z = x
    else:
        z = 3 - (x + y)
    print(z)
main()

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    print(3 - x - y)

main()
