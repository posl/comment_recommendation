Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int,input().split())

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, M = map(int, input().split())

=======
Suggestion 3

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

n, m = map(int, input().split())
a = m//n
while True:
    if m%a == 0:
        print(a)
        break
    else:
        a -= 1

=======
Suggestion 4

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

N,M=map(int,input().split())
A=[0]*N
A[0]=M
for i in range(1,N):
    A[i]=int(input())
A.sort()

ans=A[0]
for i in range(1,N):
    ans=gcd(ans,A[i])
print(ans)

=======
Suggestion 5

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
m //= n
ans = 1
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        ans = max(ans, i)
        ans = max(ans, m // i)
print(ans)

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N,M = map(int,input().split())
A = list(map(int,input().split()))

=======
Suggestion 7

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

n,m=map(int,input().split())

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = list(map(int, input().split()))
lcm = 1
for i in range(n):
    a[i] //= 2
    lcm *= a[i] // gcd(lcm, a[i])
for i in range(n):
    if (lcm // a[i]) % 2 == 0:
        print(0)
        exit()
print((m // lcm + 1) // 2)
