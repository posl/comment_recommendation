Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

g = A[0]
for i in range(1, N):
    g = gcd(g, A[i])

=======
Suggestion 2

def solve(n, a):
    a.sort()
    for i in range(n-1):
        if a[i+1] % a[i] == 0:
            a[i+1] = a[i]
        else:
            a[i+1] %= a[i]
    return a[-1]

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        a[i+1] = a[i+1] % a[i]
    print(a[-1])

=======
Suggestion 4

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

=======
Suggestion 5

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = A[0]
    for i in range(1, N):
        if ans * 2 >= A[i]:
            ans += A[i]
        else:
            ans = A[i]
    print(ans)

=======
Suggestion 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

=======
Suggestion 8

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 9

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a
