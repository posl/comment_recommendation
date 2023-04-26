Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a >= b + c:
        print(0)
    else:
        print(b + c - a)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(max(0, c - (a - b)))

=======
Suggestion 3

def main():
    A,B,C = map(int,input().split())
    if A >= B + C:
        print(0)
    else:
        print(C - (A - B))

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(C if A >= B + C else B + C - A)

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(c if a >= b + c else a + b - c)

=======
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    print(c - (a-b) if c - (a-b) > 0 else 0)

=======
Suggestion 7

def func(a,b,c):
    if b >= a:
        return c - (b - a)
    else:
        return c

a,b,c = map(int, input().split())
print(func(a,b,c))

=======
Suggestion 8

def main():
    a,b,c = map(int, input().split())
    print(c if a >= b+c else b+c-a)

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    print(c if a >= c else a - (c - b))
