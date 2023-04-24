Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)

main()

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif a == c:
        print(b)
    else:
        print(0)

=======
Suggestion 5

def solve():
    a, b, c = map(int, input().split())
    if a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return 0

print(solve())

=======
Suggestion 6

def dice_game():
    a = input()
    b = input()
    c = input()
    if a == b:
        print c
    elif a == c:
        print b
    elif b == c:
        print a
    else:
        print 0

dice_game()
