Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x,y = map(int,input().split())
    if x == y:
        print(x)
    else:
        print(3-x-y)

=======
Suggestion 2

def main(x, y):
    if x == y:
        return x
    else:
        return 3 - x - y

x, y = map(int, input().split())
print(main(x, y))

=======
Suggestion 3

def main():
    x,y = map(int,input().split())
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
Suggestion 4

def main():
    x, y = map(int, input().split())
    print((x-y) % 3)

=======
Suggestion 5

def get_opposite(x):
    return 2 if x == 0 else 0

x, y = map(int, input().split())
print(get_opposite(x) if x == y else 1 if x != get_opposite(y) else y)

=======
Suggestion 6

def get_input():
    x, y = map(int, input().split())
    return x, y

=======
Suggestion 7

def solve():
    x, y = map(int, input().split())
    print((x - y + 3) % 3)
