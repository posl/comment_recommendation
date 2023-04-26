Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    a,b,c,d = map(int,input().split())
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
    a,b,c,d = map(int,input().split())
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
Suggestion 4

def main():
    a, b, c, d = map(int, input().split())
    while True:
        c = c - b
        if c <= 0:
            print("Yes")
            break
        a = a - d
        if a <= 0:
            print("No")
            break

=======
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
    while True:
        c -= b
        if c <= 0:
            print("Yes")
            exit()
        a -= d
        if a <= 0:
            print("No")
            exit()

=======
Suggestion 6

def main():
    a,b,c,d = map(int,input().split())
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
Suggestion 7

def main():
    a,b,c,d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print('Yes')
            exit()
        a -= d
        if a <= 0:
            print('No')
            exit()

=======
Suggestion 8

def solve(A, B, C, D):
    while A > 0 and C > 0:
        C -= B
        if C <= 0:
            return "Yes"
        A -= D
        if A <= 0:
            return "No"
