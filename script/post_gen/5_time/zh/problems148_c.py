Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
x = gcd(a, b)
print(a * b // x)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

a, b = map(int, input().split())

print(lcm(a, b))

=======
Suggestion 4

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
a,b = map(int,input().split())
g = gcd(a,b)
print(a*b//g)

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    print(a*b)

=======
Suggestion 7

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b=map(int,input().split())
gcd_num=gcd(a,b)
print(a*b//gcd_num)

=======
Suggestion 8

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

a, b = map(int, input().split())
g = gcd(a, b)
for i in range(g):
    print(1, end="")
