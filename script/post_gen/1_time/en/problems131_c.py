Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def main():
    A, B, C, D = map(int, input().split())
    print((B-A+1) - B//C - B//D + B//lcm(C,D) + A//C + A//D - A//lcm(C,D) - (A-1)//C - (A-1)//D + (A-1)//lcm(C,D))
