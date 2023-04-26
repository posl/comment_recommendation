Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 4

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
a=list(set(a))
n=len(a)

l=a[0]//2
for i in range(1,n):
    l=l*a[i]//gcd(l,a[i])

ans=0
for i in range(1,m+1):
    if i%l==0:
        ans+=1

print(ans)

=======
Suggestion 5

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

N,M = map(int,input().split())
A = list(map(int,input().split()))
A = [a//2 for a in A]
lcm = 1
for a in A:
    lcm = lcm * a // gcd(lcm,a)
for a in A:
    if (lcm//a)%2==0:
        print(0)
        exit()
print((M//lcm+1)//2)
