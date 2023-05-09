Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
d = gcd(n, m)
print(m // d)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
for i in range(m // n, 0, -1):
    if m % i == 0:
        print(i)
        break

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, M = map(int, input().split())
ans = 1
for i in range(1, int(M**0.5)+1):
    if M % i == 0:
        if M // i >= N:
            ans = max(ans, i)
        if i >= N:
            ans = max(ans, M // i)
print(ans)

=======
Suggestion 7

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

n,m = map(int,input().split())

=======
Suggestion 8

def gcd(a,b):
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n,m = map(int, input().split())
m = m//n
for i in range(m,0,-1):
    if m%i == 0:
        print(i)
        break

=======
Suggestion 9

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

N,M = map(int, input().split())
for i in range(1, int(M**0.5)+1):
    if M%i == 0:
        if M//i >= N:
            ans = i
        if i >= N:
            ans = M//i

print(ans)
