Synthesizing 10/10 solutions

=======
Suggestion 1

def problems279_d():
    A, B = map(int, input().split())
    print((A + B - 1) / B)

=======
Suggestion 2

def solve(A: int, B: int):
    import math
    g = 1
    result = A
    while True:
        t = A / math.sqrt(g)
        if result < t + B:
            break
        result = t + B
        g += 1
    return result

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    print((a-1)/(2*b))

=======
Suggestion 4

def solve():
    import math
    A, B = map(int, input().split())
    print((A+B-1)/B)

=======
Suggestion 5

def solve():
    a, b = map(int, input().split())
    g = 1
    res = a
    while g < a / 2:
        t = g + a / (2 * g)
        if t < res:
            res = t
        g += b
    print(res)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print(((A+B)/2)**(1/2))

=======
Suggestion 7

def problems279_d():
    a, b = map(int, input().split())
    print((a - 1) * 1 / b)

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    print((B-1)*A/(B*B-1))

=======
Suggestion 9

def main():
    a,b = map(int, input().split())
    print((a+b)/b)

=======
Suggestion 10

def main():
    A,B = map(int,input().split())
    print(2*B+A/(B**2))
