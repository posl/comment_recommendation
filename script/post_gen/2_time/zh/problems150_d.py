Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 2

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

=======
Suggestion 3

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 4

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

=======
Suggestion 5

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

=======
Suggestion 6

def gcd(x, y):
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lcm = a[0]
for i in range(1, n):
    lcm = lcm * a[i] // gcd(lcm, a[i])
count = 0
for i in range(n):
    count += (lcm // a[i]) // 2
print(count % (10 ** 9 + 7))

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = list(map(int, input().split()))

lcm = a[0]
for i in range(1, n):
    lcm = lcm * a[i] // gcd(lcm, a[i])

for i in range(n):
    if lcm // a[i] % 2 == 0:
        print(0)
        exit()

m //= lcm
ans = (m + 1) // 2
print(ans)

=======
Suggestion 9

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 10

def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)
