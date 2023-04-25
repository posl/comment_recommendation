Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if b == sorted([a, b, c])[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def median(a, b, c):
    if a < b:
        if b < c:
            return b
        else:
            if a < c:
                return c
            else:
                return a
    else:
        if a < c:
            return a
        else:
            if b < c:
                return c
            else:
                return b

a, b, c = map(int, input().split())

=======
Suggestion 3

def median(a,b,c):
    if a > b:
        if b > c:
            return b
        elif a > c:
            return c
        else:
            return a
    else:
        if a > c:
            return a
        elif b > c:
            return c
        else:
            return b

a,b,c = map(int, input().split())
print("Yes" if median(a,b,c) == b else "No")

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a < b < c or c < b < a:
        print('Yes')
    elif a < c < b or b < c < a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if b >= a and b <= c:
        print("Yes")
    elif b >= c and b <= a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    if (a < b < c) or (c < b < a):
        print("Yes")
    elif (b < a < c) or (c < a < b):
        print("Yes")
    elif (a < c < b) or (b < c < a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def isMedian(a, b, c):
    if (a < b and b < c) or (c < b and b < a):
        return "Yes"
    else:
        return "No"

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    print("Yes" if a < b < c or c < b < a else "No")

=======
Suggestion 9

def median(a,b,c):
    if (a <= b <= c) or (c <= b <= a):
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 10

def solve(a, b, c):
    if a < b < c or c < b < a:
        return "Yes"
    return "No"
