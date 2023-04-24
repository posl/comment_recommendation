Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def median(a, b, c):
    if a < b:
        if b < c:
            return b
        elif a < c:
            return c
        else:
            return a
    else:
        if a < c:
            return a
        elif b < c:
            return c
        else:
            return b

=======
Suggestion 2

def median(a, b, c):
    if a < b < c or c < b < a:
        return 'Yes'
    elif b < a < c or c < a < b:
        return 'Yes'
    elif a < c < b or b < c < a:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if b == sorted([a, b, c])[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def median(a,b,c):
    if b < a < c or c < a < b:
        return "Yes"
    elif a < b < c or c < b < a:
        return "Yes"
    elif a < c < b or b < c < a:
        return "Yes"
    elif b == a == c:
        return "Yes"
    else:
        return "No"

=======
Suggestion 6

def median(a,b,c):
    if a > b:
        a,b = b,a
    if b > c:
        b,c = c,b
    if a > b:
        a,b = b,a
    return b

a,b,c = map(int, input().split())
print("Yes" if median(a,b,c) == b else "No")

=======
Suggestion 7

def main():
    a, b, c = [int(x) for x in input().split()]
    if b > a and b < c or b < a and b > c:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def median():
    a,b,c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")

median()
