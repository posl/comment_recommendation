Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a <= b:
        print(0)
    else:
        print(a - b * 2)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A <= B:
        print(0)
    else:
        print(A-B*2)

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    if a < b:
        print(0)
    else:
        print(a-b*2)

=======
Suggestion 4

def solve():
    a, b = map(int, input().split())
    if a > b:
        print(a - b)
    else:
        print(0)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print(max(0, A - 2*B))

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(max(0, a - (b * 2)))

=======
Suggestion 7

def problems143_a():
    a,b = map(int,input().split())
    if a <= b:
        print(0)
    else:
        print(a-b*2)

=======
Suggestion 8

def solve(a,b):
    if a < b * 2:
        return 0
    else:
        return a - b * 2

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    print(max(0,a-b*2))
