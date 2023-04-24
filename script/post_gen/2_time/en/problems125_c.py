Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

=======
Suggestion 6

def gcd(a, b): # greatest common divisor
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    if n == 2:
        print(max(a))
        return
    a.sort()
    if a[0] == a[1]:
        print(a[0])
        return
    g = a[1]
    for i in range(2,n):
        g = gcd(g,a[i])
    print(g)
