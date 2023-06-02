Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d = map(int,input().split())
    # print(a,b,c,d)
    count = 0
    for i in range(a,b+1):
        if i % c == 0 and i % d == 0:
            count += 1
    print(count)

=======
Suggestion 2

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 5

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

=======
Suggestion 6

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    return gcd(b,a%b)

=======
Suggestion 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 8

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a%b)

A, B, C, D = map(int, input().split())

=======
Suggestion 9

def main():
    a,b,c,d = map(int, input().split())
    count = 0
    for i in range(a, b+1):
        if i % c == 0 and i % d == 0:
            count += 1
    print(count)
