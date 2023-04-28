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
        return gcd(b, a % b)

N,M = map(int,input().split())
A = list(map(int,input().split()))

=======
Suggestion 3

def gcd(a, b):
    if a % b == 0:
        return(b)
    else:
        return(gcd(b, a % b))

=======
Suggestion 4

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 6

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

=======
Suggestion 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 8

def gcd(a,b):
    if a%b==0:
        return(b)
    else:
        return(gcd(b,a%b))

N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
A=list(set(A))
A.sort()
A.reverse()
B=[]
B.append(A[0])
for i in range(1,len(A)):
    if gcd(B[-1],A[i])==B[-1]:
        continue
    else:
        B.append(A[i])
A=B
#print(A)
ans=0
for i in range(len(A)):
    ans+=M//(2*A[i])
    ans-=M//(2*A[i])*2
print(ans)

=======
Suggestion 9

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

n,m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
a = list(map(lambda x: x//2, a))

lcm = a[0]
for i in range(1, n):
    lcm = lcm*a[i]//gcd(lcm, a[i])

for i in range(n):
    if ((lcm//a[i])//2)%2 == 0:
        print(0)
        exit()

print(m//lcm - m//(lcm*2))
