Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

a, b = map(int, input().split())
print(a*b//gcd(a, b))

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
g = gcd(a, b)
print(a * b // g)

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

=======
Suggestion 4

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

=======
Suggestion 5

def lcm(x, y):
    return (x * y) // gcd(x, y)

=======
Suggestion 6

def lcm(a,b):
    import fractions
    return a * b // fractions.gcd(a,b)

a,b = map(int,input().split())

print(lcm(a,b))

=======
Suggestion 7

def lcm(a, b):
    return a * b // gcd(a, b)

=======
Suggestion 8

def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x%y)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    print(a*b)
