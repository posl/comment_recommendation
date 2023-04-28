Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    V, A, B, C = map(int, input().split())
    if A > B:
        A, B = B, A
    if A > C:
        A, C = C, A
    if B > C:
        B, C = C, B
    if V < A:
        print('F')
    elif V < B:
        print('M')
    elif V < C:
        print('T')
    else:
        print('T')

=======
Suggestion 2

def main():
    V, A, B, C = map(int, input().split())
    if V < A:
        print("F")
    elif V < B:
        print("M")
    elif V < C:
        print("T")
    else:
        print("M")

=======
Suggestion 3

def main():
    V, A, B, C = map(int, input().split())
    if V % A == 0:
        print("F")
    elif V % B == 0:
        print("M")
    elif V % C == 0:
        print("T")

=======
Suggestion 4

def main():
    v,a,b,c = map(int,input().split())
    if a>b:
        a,b = b,a
    if a>c:
        a,c = c,a
    if b>c:
        b,c = c,b
    if v%a==0:
        print("F")
    elif v%b==0:
        print("M")
    elif v%c==0:
        print("T")
    else:
        print("F")

=======
Suggestion 5

def main():
    v,a,b,c = map(int, input().split())
    v -= a
    if v <= 0:
        print('F')
        return
    v -= b
    if v <= 0:
        print('M')
        return
    v -= c
    if v <= 0:
        print('T')
        return

=======
Suggestion 6

def main():
    v,a,b,c = map(int,input().split())
    if v <= a:
        print("F")
    elif v <= a+b:
        print("M")
    elif v <= a+b+c:
        print("T")

=======
Suggestion 7

def main():
    v, a, b, c = map(int, input().split())
    if v % a == 0:
        if v % b == 0:
            if v % c == 0:
                print("M")
            else:
                print("F")
        else:
            print("T")
    else:
        print("F")

=======
Suggestion 8

def main():
    V,A,B,C = [int(i) for i in input().split()]
    if A >= V:
        print('F')
    elif B >= V:
        print('M')
    elif C >= V:
        print('T')
    else:
        print('M')

=======
Suggestion 9

def main():
    V,A,B,C = map(int,input().split())
    if A + B + C <= V:
        print("M")
    elif A + B <= V:
        print("T")
    elif A <= V:
        print("F")
    else:
        print("M")

=======
Suggestion 10

def main():
    V, A, B, C = map(int, input().split())
    if A > B:
        if B > C:
            print("F")
        elif C > B:
            if V - A >= 0:
                print("T")
            else:
                print("F")
    elif B > A:
        if A > C:
            print("M")
        elif C > A:
            if V - B >= 0:
                print("T")
            else:
                print("M")
    elif A == B:
        if A > C:
            print("M")
        elif C > A:
            if V - A >= 0:
                print("T")
            else:
                print("M")
