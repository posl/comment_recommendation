Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    a,b,c,d = map(int,input().split())
    if (c-1)//b > (a-1)//d:
        print("否")
    else:
        print("是")

=======
Suggestion 3

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
Suggestion 4

def problem164_b():
    A, B, C, D = map(int, input().split())
    while True:
        C = C - B
        if C <= 0:
            print('Yes')
            break
        A = A - D
        if A <= 0:
            print('No')
            break

=======
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
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
Suggestion 6

def main():
    a, b, c, d = map(int, input().strip().split())
    while True:
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d
        if a <= 0:
            print("No")
            break
