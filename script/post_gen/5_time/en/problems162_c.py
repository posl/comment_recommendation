Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

K=int(input())
ans=0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            ans+=gcd(gcd(a,b),c)
print(ans)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

K = int(input())
ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            ans += gcd(a, gcd(b, c))
print(ans)

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

K = int(input())
ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            ans += gcd(gcd(a, b), c)
print(ans)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

K = int(input())
ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        tmp = gcd(a, b)
        for c in range(1, K + 1):
            ans += gcd(tmp, c)
print(ans)

=======
Suggestion 5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 6

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
k=int(input())
ans=0
for i in range(1,k+1):
    for j in range(1,k+1):
        for l in range(1,k+1):
            ans+=gcd(gcd(i,j),l)
print(ans)

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 8

def gcd(x, y):
  if x < y:
    x, y = y, x
  if y == 0:
    return x
  return gcd(y, x % y)

K = int(input())
ans = 0
for a in range(1, K+1):
  for b in range(1, K+1):
    for c in range(1, K+1):
      ans += gcd(gcd(a, b), c)
print(ans)

=======
Suggestion 9

def gcd(x,y):
    if x == 0:
        return y
    else:
        return gcd(y%x, x)

K = int(input())

ans = 0

for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            ans += gcd(a, gcd(b,c))

print(ans)
