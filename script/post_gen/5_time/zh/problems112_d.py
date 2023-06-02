Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n,m=map(int,input().split())

print(gcd(n,m))

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n,m = map(int, input().split())
for i in range(1, int(m/n)+1):
    if m % i == 0:
        if i * n <= m:
            ans = i
print(ans)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())

=======
Suggestion 4

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

N,M=map(int,input().split())

=======
Suggestion 5

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

N,M=map(int,input().split())
#M=10**9

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n, m = map(int, input().split())

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
# n, m = 10, 123
# n, m = 100000, 1000000000
# n, m = 3, 14
# n, m = 3, 6
# n, m = 3, 7
# n, m = 3, 8
# n, m = 3, 9
# n, m = 3, 10
# n, m = 3, 11
# n, m = 3, 12
# n, m = 3, 13
# n, m = 3, 14
# n, m = 3, 15
# n, m = 3, 16
# n, m = 3, 17
# n, m = 3, 18
# n, m = 3, 19
# n, m = 3, 20
# n, m = 3, 21
# n, m = 3, 22
# n, m = 3, 23
# n, m = 3, 24
# n, m = 3, 25
# n, m = 3, 26
# n, m = 3, 27
# n, m = 3, 28
# n, m = 3, 29
# n, m = 3, 30
# n, m = 3, 31
# n, m = 3, 32
# n, m = 3, 33
# n, m = 3, 34
# n, m = 3, 35
# n, m = 3, 36
# n, m = 3, 37
# n, m = 3, 38
# n, m = 3, 39
# n, m = 3, 40
# n, m = 3, 41
# n, m = 3, 42
# n, m = 3, 43
# n, m =

=======
Suggestion 8

def gcd(a,b):
    if a<b:
        a,b=b,a
    while a%b!=0:
        a,b=b,a%b
    return b


N,M=map(int,input().split())
a=gcd(N,M)
print(M//a)

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
