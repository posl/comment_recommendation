Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2]-a[1] == a[1]-a[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    a,b,c = map(int, input().split())
    if (b - a == c - b):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    a = sorted(list(map(int, input().split())))
    if (a[2] - a[1]) == (a[1] - a[0]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if a - b == b - c:
        print('Yes')
    elif a - c == c - b:
        print('Yes')
    elif b - a == a - c:
        print('Yes')
    elif b - c == c - a:
        print('Yes')
    elif c - a == a - b:
        print('Yes')
    elif c - b == b - a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
    if a - b == b - c or a - c == c - b or b - a == a - c or b - c == c - a or c - a == a - b or c - b == b - a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print("Yes")
    else:
        print("No")

main()
