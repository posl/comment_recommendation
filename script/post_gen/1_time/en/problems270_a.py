Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print(A + B - max(A, B) + 1)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(7 - A - B)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(A + B + max(0, A - 1) + max(0, B - 1))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(a + b + max(a, b))

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print(A + B - (A & B))

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    print(A+B-max(A,B))

main()

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    print(a+b+max(a,b))

main()

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print(a + b + max(0, a+b-6))

=======
Suggestion 9

def solve(a, b):
    return a + b + (a & b)
