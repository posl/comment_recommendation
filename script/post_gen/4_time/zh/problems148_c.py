Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
print(a * b // gcd(a, b))

=======
Suggestion 2

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

a,b = map(int,input().split())
g = gcd(a,b)
l = a*b//g
print(l)

=======
Suggestion 3

def getMinSnack(A, B):
    if A < B:
        min = A
    else:
        min = B
    while True:
        if A % min == 0 and B % min == 0:
            break
        min -= 1
    return min

input = input().split()
A = int(input[0])
B = int(input[1])

min = getMinSnack(A, B)
print(A*B//min)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print(A*B)

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

A, B = map(int,input().split())
C = gcd(A, B)
D = A * B / C
print(int(D))

=======
Suggestion 6

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

=======
Suggestion 7

def gcd(a,b): #最大公约数
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 8

def gcd(a, b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 9

def get_min(a,b):
    if a == b:
        return a
    else:
        return a*b
