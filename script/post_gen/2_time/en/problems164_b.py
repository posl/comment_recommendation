Synthesizing 10/10 solutions

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

def main():
    A,B,C,D = map(int,input().split())
    while A > 0 and C > 0:
        C -= B
        if C <= 0:
            print('Yes')
            break
        A -= D
        if A <= 0:
            print('No')
            break

=======
Suggestion 4

def main():
    A, B, C, D = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    
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
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
    while(True):
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
    a, b, c, d = map(int, input().split())
    if (c + d - 1) // d >= (a + b - 1) // b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a,b,c,d = map(int, input().split())
    if (c+b-1)//b <= (a+d-1)//d:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    A, B, C, D = map(int, input().split())
    if A <= D * C:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    A,B,C,D = map(int, input().split())
    if (B >= C and D >= A):
        print("Yes")
    elif (B >= C and D >= A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    #get input
    A, B, C, D = map(int, input().split())

    #calculate
    if B >= C*D:
        print("No")
    else:
        print("Yes")
