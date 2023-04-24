Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if b <= max(a, c) and b >= min(a, c):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a < b < c or c < b < a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if (a < b < c) or (c < b < a):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if b < a < c or c < a < b:
        print("Yes")
    elif a < b < c or c < b < a:
        print("Yes")
    elif a < c < b or b < c < a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if a < b < c or c < b < a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    if a > b:
        if b > c:
            print("Yes")
        elif a > c:
            print("Yes")
        else:
            print("No")
    elif a < b:
        if a > c:
            print("No")
        elif b > c:
            print("No")
        else:
            print("Yes")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    abclist = list(map(int, input().split()))
    abclist.sort()
    if abclist[1] == abclist[0] or abclist[1] == abclist[2]:
        print("Yes")
    else:
        print("No")
