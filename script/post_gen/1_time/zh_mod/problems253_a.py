Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if b == max(a, b, c) or b == min(a, b, c):

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if b < a:
        a,b = b,a
    if c < b:
        b,

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if a <= b <= c or c <= b <= a:
        print('Yes')

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if b>=a and b<=c:
        print("Yes")
    elif b>=c

=======
Suggestion 6

def main():
    a,b,c = map(int, raw_input().split())
    list = [a,b,c]
    list.sort()
    if b == list

=======
Suggestion 7

def find_mid(a,b,c):
    if a<b<c or c<b<a:
        return b
    elif b<a<c or c<a<b:
        return a

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    if a<=b<=c or c<=b<=a:
        print('Yes')
    else

=======
Suggestion 9

def median(a,b,c):
    if a <= b <= c or c <= b <= a:
        return True
    else:
        return False
