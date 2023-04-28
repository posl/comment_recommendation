Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    AB = input().split()
    A = int(AB[0])
    B = int(AB[1])
    CD = input().split()
    C = int(CD[0])
    D = int(CD[1])
    while True:
        C = C - B
        if C <= 0:
            print("Yes")
            break
        A = A - D
        if A <= 0:
            print("No")
            break

=======
Suggestion 2

def main():
    a,b,c,d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d
        if a <= 0:
            print("No")
            break

=======
Suggestion 3

def main():
    a, b, c, d = map(int, input().split())
    while a > 0 and c > 0:
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d
        if a <= 0:
            print("No")
            break

=======
Suggestion 4

def main():
    a, b, c, d = map(int, input().split())
    while a > 0 and c > 0:
        c -= b
        if c <= 0:
            print('Yes')
            break
        a -= d
        if a <= 0:
            print('No')
            break

=======
Suggestion 5

def main():
    A,B,C,D = map(int, input().split())
    while True:
        C -= B
        if C <= 0:
            print("Yes")
            break
        A -= D
        if A <= 0:
            print("No")
            break

=======
Suggestion 6

def main():
    a, b, c, d = map(int, input().split())
    while a > 0 and c > 0:
        c -= b
        if c <= 0:
            print('Yes')
            return
        a -= d
        if a <= 0:
            print('No')
            return

=======
Suggestion 7

def main():
    a,b,c,d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print('Yes')
            return
        a -= d
        if a <= 0:
            print('No')
            return

=======
Suggestion 8

def problem():
    a,b,c,d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print("Yes")
            return
        a -= d
        if a <= 0:
            print("No")
            return

=======
Suggestion 9

def main():
    a,b,c,d = map(int,input().split())
    while a>0 and c>0:
        c-=b
        if c<=0:
            print("Yes")
            exit()
        a-=d
    print("No")

=======
Suggestion 10

def main():
    AB, CD = map(int, input().split())
    if AB * CD > 0:
        print('Yes')
    else:
        print('No')
