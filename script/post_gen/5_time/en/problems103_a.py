Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(max(a, b, c) - min(a, b, c))

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[1] - a[0] + a[2] - a[1])

=======
Suggestion 3

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] - A[0])

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(min(abs(a-b)+abs(b-c), abs(a-c)+abs(b-c), abs(a-b)+abs(a-c)))

=======
Suggestion 6

def problems103_a():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] - A[0])

=======
Suggestion 7

def solve():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 8

def main():
    a = sorted(map(int, input().split()))
    print(a[2] - a[0])

=======
Suggestion 9

def main():
    cost = 0
    a = list(map(int, input().split()))
    a.sort()
    cost = a[2] - a[0]
    print(cost)

=======
Suggestion 10

def main():
    a = input()
    b = a.split()
    b = list(map(int, b))
    b.sort()
    print(b[2] - b[0])
