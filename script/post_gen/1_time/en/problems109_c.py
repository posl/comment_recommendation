Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
D = x[1] - x[0]
for i in range(1, N):
    D = gcd(D, x[i+1] - x[i])
print(D)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1]-x[i])
    d.sort()
    ans = d[0]
    for i in range(1, N):
        ans = gcd(ans, d[i])
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1] - x[i])
    import fractions
    ans = d[0]
    for i in range(1,N):
        ans = fractions.gcd(ans,d[i])
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1]-x[i])
    gcd = d[0]
    for i in range(1, N):
        gcd = gcd2(gcd, d[i])
    print(gcd)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()

    ans = x[1] - x[0]
    for i in range(1, len(x) - 1):
        ans = gcd(ans, x[i + 1] - x[i])

    print(ans)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    d = abs(X - x[0])
    for i in range(1, N):
        d = gcd(d, abs(X - x[i]))
    print(d)

=======
Suggestion 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 8

def solve():
    N,X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1]-x[i])
    d.sort()
    ans = d[0]
    for i in range(N-1):
        ans = gcd(ans,d[i+1])
    print(ans)

=======
Suggestion 9

def solve():
    N, X = map(int, input().split())
    xs = list(map(int, input().split()))
    xs.append(X)
    xs.sort()
    ds = [xs[i+1] - xs[i] for i in range(N)]
    d = ds[0]
    for i in range(1, N):
        d = gcd(d, ds[i])
    print(d)

=======
Suggestion 10

def solve(N,X,x):
    x.append(X)
    x.sort()
    D = x[1]-x[0]
    for i in range(1,N):
        D = gcd(D,x[i+1]-x[i])
    return D
