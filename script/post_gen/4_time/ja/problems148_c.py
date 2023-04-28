Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input().split())
g = gcd(a, b)
print(a * b // g)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a,b = map(int,input().split())
print(a*b//gcd(a,b))

=======
Suggestion 4

def gcd(a,b):
    if a<b:
        a,b = b,a
    while b:
        a,b = b,a%b
    return a

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A
    for i in range(B, (A*B)+1):
        if i % A == 0 and i % B == 0:
            print(i)
            break

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
    
a,b = map(int, input().split())
print(a*b//gcd(a,b))

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    if A>B:
        A,B = B,A
    for i in range(B,1000000000):
        if A*i%B==0:
            print(A*i)
            break

=======
Suggestion 8

def lcm(x,y):
    return x*y//gcd(x,y)
