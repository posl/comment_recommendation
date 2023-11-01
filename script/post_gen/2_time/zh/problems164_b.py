Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d = map(int, input().split())
    while a>0 and c>0:
        c -= b
        if c <= 0:
            print("Yes")
            break

=======
Suggestion 2

def main():
    A, B, C, D = map(int, input().split())
    while True:
        C -= B
        if C <= 0:
            print("Yes")
            break
        A -= D

=======
Suggestion 3

def battle(a,b,c,d):
    while True:
        c = c - b
        if c <= 0:
            return 'Yes'
        a = a - d
        if a <= 0:
            return 'No'

=======
Suggestion 4

def main():
    a,b,c,d = map(int,input().split(' '))
    while True:
        c -= b
        if c <= 0:
            print('Yes')
            break
        a -= d

=======
Suggestion 5

def main():
    a,b,c,d = map(int, input().split())
    while True:
        c = c-b
        if c <= 0:
            print("Yes")
            break
        a = a-d

=======
Suggestion 6

def main():
    a,b,c,d = map(int,input().split())
    while True:
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d

=======
Suggestion 7

def main():
    a,b,c,d=map(int,input().split())
    while True:
        c=c-b
        if c<=0:
            print('Yes')
            break
        a=a-d

=======
Suggestion 8

def main():
    a,b,c,d = map(int,input().split())
    while a > 0 and c > 0:
        c -= b
        a -= d
    if c <= 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    a,b,c,d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print('Yes')
            break
        a -= d
