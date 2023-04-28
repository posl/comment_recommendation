Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

N, M = map(int, input().split())

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

N, M = map(int, input().split())

=======
Suggestion 4

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n,m=map(int,input().split())

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, M = map(int, input().split())
print(gcd(N, M))

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, M = map(int, input().split())
ans = 1
for i in range(2, min(M//N+1, M+1)):
    if M % i == 0:
        ans = max(ans, i)
        while M % i == 0:
            M //= i

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
g = a[0]
for i in range(n):
    g = gcd(g, a[i])
print(g)

=======
Suggestion 8

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n,m = map(int,input().split())
a = m//n
while True:
    if m%a == 0:
        print(a)
        break
    a -= 1

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = [m // n] * n
