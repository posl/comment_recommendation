Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def median(a,b,c):
    if a<=b<=c or c<=b<=a:
        return True
    else:
        return False

=======
Suggestion 3

def is_median(a,b,c):
    if a <= b <= c or c <= b <= a:
        return True
    return False

a,b,c = map(int,input().split())

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    array = [a, b, c]
    array.sort()
    if array[1] == b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    if (b >= a and b <= c) or (b <= a and b >= c):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if (a <= b and b <= c) or (c <= b and b <= a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def median(a, b, c):
    if a <= b <= c or c <= b <= a:
        return True
    else:
        return False

a, b, c = map(int, input().split())

=======
Suggestion 9

def problem253_a():
    a,b,c = map(int,input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")
