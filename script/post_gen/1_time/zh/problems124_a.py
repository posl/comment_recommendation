Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def coins(a,b):
    if a>b:
        return a+a-1
    elif a<b:
        return b+b-1
    else:
        return a+b

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(max(a + a - 1, a + b, b + b - 1))

=======
Suggestion 3

def problems124_a():
    A, B = map(int, input().split())
    print(max(A + A - 1, B + B - 1, A + B))

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a == b:
        print(a*2)
    else:
        print(max(a,b)*2-1)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A > B:
        print(A + A - 1)
    elif A < B:
        print(B + B - 1)
    else:
        print(A + B)

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if A == B:
        print(A+B)
    elif A > B:
        print(2*A-1)
    else:
        print(2*B-1)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a == b:
        print(a+b)
    elif a > b:
        print(a+a-1)
    else:
        print(b+b-1)
