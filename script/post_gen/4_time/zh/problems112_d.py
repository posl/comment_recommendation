Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
n, m = map(int, input().split())

for i in range(m//n, 0, -1):
    if m%i == 0:
        print(i)
        break

=======
Suggestion 2

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n,m = map(int,input().split())
# n,m = 10,123

=======
Suggestion 3

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

N,M = map(int,input().split())
ans = 1
for i in range(1,int(M**0.5)+1):
    if M % i == 0:
        if i * N <= M:
            ans = max(ans,i)
        if (M // i) * N <= M:
            ans = max(ans,M//i)

print(ans)

=======
Suggestion 4

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

n,m=map(int,input().split())

=======
Suggestion 5

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n, m = map(int, input().split())
#n, m = 3, 14
#n, m = 10, 123
#n, m = 100000, 1000000000

=======
Suggestion 7

def gcd(a,b):
    if a<b:
        a,b = b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n,m = map(int,input().split())

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n, m = map(int, input().split())
