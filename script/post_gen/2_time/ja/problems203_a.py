Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif a == c:
        print(b)
    else:
        print(0)

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)

=======
Suggestion 4

def main():
    dice = list(map(int, input().split()))
    dice.sort()
    if dice[0] == dice[1]:
        print(dice[2])
    elif dice[1] == dice[2]:
        print(dice[0])
    else:
        print(0)

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    if a==b and a==c:
        print(a)
    elif a==b:
        print(c)
    elif b==c:
        print(a)
    elif a==c:
        print(b)
    else:
        print(0)
