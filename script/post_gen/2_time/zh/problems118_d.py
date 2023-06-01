Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    while len(A) > 1:
        A = [a % min(A) for a in A if a % min(A) > 0]
    print(min(A))

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[0]
    for i in range(1, n):
        ans = gcd(ans, a[i])
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        if A[i+1] % A[i] != 0:
            A[i+1] %= A[i]
    print(A[N-1])
solve()

=======
Suggestion 5

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

n = int(input())
a = list(map(int, input().split()))
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
print(g)

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        r = a % b
        a, b = b, r
    return a

n = int(input())
a = list(map(int, input().split()))
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
print(g)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    import fractions
    ans = A[0]
    for i in range(1, N):
        ans = fractions.gcd(ans, A[i])
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    import fractions
    def gcd_list(numbers):
        return functools.reduce(fractions.gcd, numbers)
    print(gcd_list(A))

=======
Suggestion 9

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
