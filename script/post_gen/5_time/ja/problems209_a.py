Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print(B-A+1 if B>=A else 0)

=======
Suggestion 2

def count(a,b):
    n = 0
    for i in range(a,b+1):
        n += 1
    return n

a,b = map(int,input().split())
print(count(a,b))

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    print(max(0,b-a+1))

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a > b:
        print(0)
    else:
        print(b-a+1)

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    if a >= b:
        print(0)
    else:
        print(b-a+1)

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    if b >= a:
        print(b - a + 1)
    else:
        print(0)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print(b - a + 1)

=======
Suggestion 8

def problems209_a(A, B):
    print(B-A+1)
