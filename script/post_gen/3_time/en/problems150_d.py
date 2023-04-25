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
        return gcd(b, a % b)

=======
Suggestion 3

def gcd(a, b):
    while b != 0:
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
    if a < b:
        a, b = b, a
    if b == 0: return a
    return gcd(b, a % b)

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = list(map(int, input().split()))
g = a[0]
for i in range(n):
    g = gcd(g, a[i])
for i in range(n):
    if (a[i] // 2) % g == 0:
        print(0)
        exit()
print((m // g + 1) // 2)

=======
Suggestion 7

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = list(map(lambda x: x//2, A))
    lcm = A[0]
    for a in A[1:]:
        lcm = lcm * a // gcd(lcm, a)
    if lcm > M:
        return 0
    return (M//lcm+1)//2
