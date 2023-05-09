Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def main():
    A, B, C, D = map(int, input().split())
    count = 0
    for i in range(A, B + 1):
        if i % C != 0 and i % D != 0:
            count += 1
    print(count)

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

=======
Suggestion 4

def main():
    A,B,C,D = map(int, input().split())
    x = B//C - (A-1)//C
    y = B//D - (A-1)//D
    z = B//(C*D) - (A-1)//(C*D)
    print(B-A+1-x-y+z)

=======
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
    def gcd(a,b):
        while b:
            a,b = b,a%b
        return a
    def lcm(a,b):
        return a*b//gcd(a,b)
    def f(x):
        return x - x//c - x//d + x//lcm(c,d)
    print(f(b)-f(a-1))

=======
Suggestion 6

def main():
    A, B, C, D = map(int, input().split())
    import math
    def lcm(x, y):
        return (x * y) // math.gcd(x, y)
    def f(x):
        return x - (x // C + x // D - x // lcm(C, D))
    print(f(B) - f(A - 1))

=======
Suggestion 7

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

=======
Suggestion 8

def solve(A,B,C,D):
    # write your code here
    return 0
