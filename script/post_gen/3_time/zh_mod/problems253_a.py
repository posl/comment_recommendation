Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    if ((a <= b and b <= c) or (c <= b and b <=

=======
Suggestion 2

def problems253_a(a,b,c):
    if b == a or b == c:
        return "Yes"
    else:
        return "No"

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if b == max(a,b,c) or b == min(a,b,c):

=======
Suggestion 4

def main():
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if b>=a and b<=c

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if b < a:
        a, b = b, a
    if c <

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    if a<=b<=c or c<=b<=a:
        print("Yes")

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
    if a > b:
        tmp = a
        a = b

=======
Suggestion 8

def median(a,b,c):
    if a<=b<=c or c<=b<=a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[1] == a[0] + a[2]:

=======
Suggestion 10

def med(a,b,c):
    if b >= a and b <= c:
        return True
    elif b <= a and b >= c:
        retu
