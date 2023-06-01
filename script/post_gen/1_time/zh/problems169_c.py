Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B = input().split()
    print(int(int(A)*float(B)))

=======
Suggestion 2

def main():
    A, B = map(float, input().split())
    print(int(A * B))

=======
Suggestion 3

def main():
    A, B = map(float, input().split())
    C = A * B
    print(int(C))

=======
Suggestion 4

def main():
    a,b = input().split()
    a = int(a)
    b = float(b)
    print(int(a*b))

=======
Suggestion 5

def mul(a, b):
    a = int(a)
    b = float(b)
    c = a * b
    return int(c)

=======
Suggestion 6

def main():
    a,b = input().split()
    a = int(a)
    b = float(b)
    b = int(b * 100)
    print(a*b//100)

=======
Suggestion 7

def main():
    a,b = map(float,input().split())
    print(int(a*b))

=======
Suggestion 8

def calc(A,B):
    #print(A,B)
    A = int(A)
    B = int(B*100)
    #print(A,B)
    return A*B//100

=======
Suggestion 9

def solve():
    A, B = map(float, input().split())
    print(int(A * B))
