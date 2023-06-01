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

def main():
    x, y = map(int, input().split())
    print((x + 1) % 3 if x == y else 3 - x - y)

=======
Suggestion 3

def janken(x, y):
    if x == 0 and y == 1:
        return 2
    if x == 0 and y == 2:
        return 0
    if x == 1 and y == 0:
        return 0
    if x == 1 and y == 2:
        return 1
    if x == 2 and y == 0:
        return 2
    if x == 2 and y == 1:
        return 1

x, y = map(int, input().split())
print(janken(x, y))

=======
Suggestion 4

def f(x,y):
    if x==0 and y==1:
        print(2)
    elif x==0 and y==2:
        print(0)
    elif x==1 and y==0:
        print(0)
    elif x==1 and y==2:
        print(1)
    elif x==2 and y==0:
        print(1)
    elif x==2 and y==1:
        print(2)
    else:
        print(x)
x,y=map(int,input().split())
f(x,y)

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    print((y - x + 3) % 3)

=======
Suggestion 6

def main():
    x,y = map(int, input().split())
    print(3-x-y)

=======
Suggestion 7

def main():
    x,y = map(int, input().split())
    print((x-y)%3)

=======
Suggestion 8

def solve():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)
