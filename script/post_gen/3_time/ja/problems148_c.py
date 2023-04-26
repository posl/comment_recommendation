Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
c = gcd(a, b)
print(a * b // c)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
g = gcd(a, b)
print(a*b//g)

=======
Suggestion 4

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
g = gcd(a, b)
print(a * b // g)

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 6

def lcm(x, y):
    return (x * y) // gcd(x, y)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    for i in range(1, b+1):
        if (a*i)%b == 0:
            print(a*i)
            break

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print((a * b) // math.gcd(a, b))

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    print(a*b)

=======
Suggestion 10

def solve():
    a,b = map(int,input().split())
    x = a*b
    for i in range(1,100000):
        if i*a%b==0:
            print(i*a)
            return
        if i*b%a==0:
            print(i*b)
            return
    print(x)
