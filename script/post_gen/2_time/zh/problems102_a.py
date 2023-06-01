Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print(2*n)

=======
Suggestion 2

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a % b)

N = int(input())
print(int(N/gcd(2,N)))

=======
Suggestion 3

def main():
    N = int(input())
    print(N*2)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
print((2 * n) // gcd(2, n))

=======
Suggestion 5

def problems102_a(n):
    i = 1
    while True:
        if i % n == 0 and i % 2 == 0:
            return i
        else:
            i += 1

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

N = int(input())
print(int(2*N/gcd(2,N)))

=======
Suggestion 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
print(2 * n // gcd(2, n))

=======
Suggestion 8

def func(n):
    for i in range(1, n):
        if i % 2 == 0 and i % n == 0:
            return i
    return n * 2

print(func(999999999))

=======
Suggestion 9

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
print(n * 2 // gcd(n, 2))
