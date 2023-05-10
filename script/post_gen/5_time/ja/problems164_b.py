Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c, d = map(int, input().split())
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
Suggestion 2

def main():
    A, B, C, D = map(int, input().split())
    while True:
        C -= B
        if C <= 0:
            print('Yes')
            break
        A -= D
        if A <= 0:
            print('No')
            break

=======
Suggestion 3

def attack(a,b):
    return (a+b-1)//b

a,b,c,d = map(int,input().split())

=======
Suggestion 4

def main():
    a,b,c,d = map(int,input().split())
    while a > 0 and c > 0:
        c -= b
        if c <= 0:
            print("Yes")
            exit()
        a -= d
        if a <= 0:
            print("No")
            exit()

=======
Suggestion 5

def attack(a,b):
    return (a-1)//b+1

=======
Suggestion 6

def main():
    a, b, c, d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print('Yes')
            break
        a -= d
        if a <= 0:
            print('No')
            break

=======
Suggestion 7

def judge(A,B,C,D):
    while True:
        C = C - B
        if C <= 0:
            return True
        A = A - D
        if A <= 0:
            return False

=======
Suggestion 8

def main():
    A, B, C, D = map(int, input().split())
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
Suggestion 9

def main():
    A, B, C, D = map(int, input().split())
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
Suggestion 10

def main():
    a,b,c,d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print("Yes")
            exit()
        a -= d
        if a <= 0:
            print("No")
            exit()
