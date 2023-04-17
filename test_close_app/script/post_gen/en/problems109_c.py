Synthesizing 10/10 solutions (Duplicates hidden)

=======

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
d = []
for i in range(N):
    d.append(x[i+1] - x[i])
print(gcd(d[0], d[1]))

The following code is the solution for the problem “ABC 081 B - Shift only” on the AtCoder website.

=======

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, X = map(int, input().split())
x = list(map(int, input().split()))

d = []
for i in range(N):
    d.append(abs(x[i] - X))

ans = d[0]
for i in range(1, N):
    ans = gcd(ans, d[i])

print(ans)

=======

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

=======

def solve():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    d = x[1] - x[0]
    for i in range(1, N):
        d = gcd(d, x[i] - x[i-1])
    print(d)

=======

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

=======

def main():
    N, X = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]

    x.sort()
    d = [x[i + 1] - x[i] for i in range(N - 1)]
    d.append(X - x[0])
    d.append(x[-1] - X)

    ans = d[0]
    for i in range(1, N):
        ans = gcd(ans, d[i])

    print(ans)

=======

def main():
    # input
    N, X = map(int, input().split())
    xs = list(map(int, input().split()))
    # compute
    ds = [abs(x-X) for x in xs]
    d = ds[0]
    for i in range(1, N):
        d = gcd(d, ds[i])
    # output
    print(d)
