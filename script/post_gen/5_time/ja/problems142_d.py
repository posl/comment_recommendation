Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b = map(int, input().split())
g = gcd(a, b)

ans = 1
for i in range(2, int(g**0.5)+1):
    if g % i == 0:
        ans += 1
        while g % i == 0:
            g //= i

=======
Suggestion 2

def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(b % a, a)

=======
Suggestion 3

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 4

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

A, B = map(int, input().split())

C = gcd(A, B)

ans = 1
for i in range(2, int(C ** (1 / 2)) + 1):
    if C % i == 0:
        ans += 1
        if C // i != i:
            ans += 1

print(ans)

=======
Suggestion 5

def gcd(a, b):
  if a < b:
    a, b = b, a
  if b == 0:
    return a
  return gcd(b, a % b)

A, B = map(int, input().split())
g = gcd(A, B)

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
