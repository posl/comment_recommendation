Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print(n*2)

=======
Suggestion 2

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

=======
Suggestion 3

def solve(n):
    return n * 2

=======
Suggestion 4

def problem102_a(n):
    i = 1
    while True:
        if i % 2 == 0 and i % n == 0:
            break
        i += 1
    return i

=======
Suggestion 5

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 7

def main():
    N = int(input())
    print(2*N)

=======
Suggestion 8

def gcd(x,y):
    if x < y:
        x,y = y,x
    while y > 0:
        r = x%y
        x = y
        y = r
    return x

=======
Suggestion 9

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n = int(input())
print(n * 2 // gcd(2, n))
