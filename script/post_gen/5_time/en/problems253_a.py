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
    if b == max(a, b, c) or b == min(a, b, c):
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[1] == a[0] + a[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if b == sorted([a, b, c])[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    if b > a and b < c or b < a and b > c:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def is_median(a,b,c):
    if a <= b <= c or c <= b <= a:
        return True
    else:
        return False

=======
Suggestion 7

def median(a, b, c):
    if b > a and b < c:
        return True
    elif b < a and b > c:
        return True
    return False

print("Yes" if median(*map(int, input().split())) else "No")

=======
Suggestion 8

def median(a,b,c):
    if (b>a and b<c) or (b<a and b>c):
        return True
    else:
        return False
a,b,c = map(int,input().split())
