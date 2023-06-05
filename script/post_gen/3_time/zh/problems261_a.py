Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 < l2:
        if r1 < l2:
            print(0)
        elif r1 < r2:
            print(r1 - l2)
        else:
            print(r2 - l2)
    elif l1 < r2:
        if r1 < r2:
            print(r1 - l1)
        else:
            print(r2 - l1)
    else:
        print(0)

=======
Suggestion 2

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if r1 < l2 or r2 < l1:
        print(0)
    else:
        print(min(r1,r2)-max(l1,l2))

=======
Suggestion 3

def main():
    l1,r1,l2,r2 = input().split()
    l1 = int(l1)
    r1 = int(r1)
    l2 = int(l2)
    r2 = int(r2)
    if l1<=l2 and l2<r1 and r1<=r2:
        print(r1-l2)
    elif l1<=l2 and l2<r1 and r2<r1:
        print(r2-l2)
    elif l1<=l2 and r2<=r1:
        print(r2-l2)
    elif l2<=l1 and r1<=r2:
        print(r1-l1)
    elif l2<=l1 and r1<r2:
        print(r1-l1)
    elif l2<=l1 and r2<=r1:
        print(r2-l1)
    else:
        print(0)
main()

=======
Suggestion 4

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 >= r2 or r1 <= l2:
        print(0)
    else:
        print(min(r1, r2) - max(l1, l2))

=======
Suggestion 5

def main():
    l1,r1,l2,r2 = map(int, input().split())
    if l1 <= l2 and l2 < r1:
        if r1 < r2:
            print(r1 - l2)
        else:
            print(r2 - l2)
    elif l2 <= l1 and l1 < r2:
        if r2 < r1:
            print(r2 - l1)
        else:
            print(r1 - l1)
    else:
        print(0)

=======
Suggestion 6

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l2 < r1 and r2 > l1:
        print(min(r1, r2) - max(l1, l2))
    else:
        print(0)

=======
Suggestion 7

def main():
    l1, r1, l2, r2 = map(int, input().split())
    l = max(l1, l2)
    r = min(r1, r2)
    print(max(0, r - l))

=======
Suggestion 8

def main():
    line = input()
    l1, r1, l2, r2 = map(int, line.split())
    if l1 <= l2 and l2 <= r1:
        if r1 <= r2:
            print(r1 - l2)
        else:
            print(r2 - l2)
    elif l2 <= l1 and l1 <= r2:
        if r2 <= r1:
            print(r2 - l1)
        else:
            print(r1 - l1)
    else:
        print(0)

=======
Suggestion 9

def solve():
    l1, r1, l2, r2 = map(int, input().split())
    if r1 <= l2 or r2 <= l1:
        print(0)
    else:
        print(min(r1, r2) - max(l1, l2))

=======
Suggestion 10

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if (l2 >= r1 or r2 <= l1):
        print(0)
    else:
        print(min(r1, r2) - max(l1, l2))
