Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    x = A / (A**2 + B**2)**0.5
    y = B / (A**2 + B**2)**0.5
    print(x, y)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    d = (A**2 + B**2)**0.5
    print(A/d, B/d)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(A / (A + B), B / (A + B))

main()

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(a / (a + b), b / (a + b))

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print(A / (A + B), B / (A + B))

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    dist = (a**2 + b**2)**0.5
    print(a / dist, b / dist)

=======
Suggestion 7

def main():
    import math
    a, b = map(int, input().split())
    c = math.sqrt(a**2 + b**2)
    print(a/c, b/c)
