Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int, input().split())
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)
    return

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())

    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)

=======
Suggestion 3

def solve():
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)

=======
Suggestion 4

def main():
    a,b,c = map(int, input().split())
    if a == b:
        print(c)
    elif a == c:
        print(b)
    else:
        print(0)

=======
Suggestion 5

def main():
    a = list(map(int, input().strip().split()))
    if a[0] == a[1]:
        print(a[2])
    elif a[0] == a[2]:
        print(a[1])
    elif a[1] == a[2]:
        print(a[0])
    else:
        print(0)

=======
Suggestion 6

def dice(a,b,c):
    if a==b:
        return c
    elif b==c:
        return a
    elif c==a:
        return b
    else:
        return 0

a,b,c = map(int, input().split())
print(dice(a,b,c))

=======
Suggestion 7

def func(a,b,c):
    if a==b:
        return c
    elif a==c:
        return b
    elif b==c:
        return a
    else:
        return 0

a,b,c = map(int,input().split())
print(func(a,b,c))

=======
Suggestion 8

def main():
    input = sys.stdin.readline
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    else:
        print(0)

=======
Suggestion 9

def main():
    # input
    a,b,c = map(int, input().split())

    # compute

    # output
    if a==b:
        print(c)
    elif a==c:
        print(b)
    elif b==c:
        print(a)
    else:
        print(0)
