Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print((A + B) ** 0.5 - B)

=======
Suggestion 2

def solve():
    A, B = map(int, input().split())
    if B == 1:
        print(A)
    else:
        print((A - 1) / (B - 1))
solve()

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print((A-1)/(2*B)+1)

=======
Suggestion 4

def problems279_d():
    a, b = map(int, input().split())
    print((a + 1) / b)

=======
Suggestion 5

def solve():
    A, B = map(int, input().split())
    print((A/B)**0.5)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print((A-1)*B)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print((a + b) / (b + 1))

=======
Suggestion 8

def solve():
    A, B = map(int, input().split())
    print((A*2+B)/2)

=======
Suggestion 9

def solve(A,B):
    import math
    return (A+B)/2 - B/(2*math.sqrt((A+B)/B))
