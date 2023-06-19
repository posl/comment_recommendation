Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 2

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n,m=map(int,input().split())

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

N,M=map(int,input().split())
i=1
ans=0
while i*i<=M:
    if M%i==0:
        if M//i>=N:
            ans=max(ans,i)
        if i>=N:
            ans=max(ans,M//i)
    i+=1
print(ans)

=======
Suggestion 4

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
for i in range(m // n, 0, -1):
    if m % i == 0 and gcd(i, m // i) == 1:
        print(i)
        break

=======
Suggestion 5

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 7

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

n,m = map(int,input().split())
for i in range(int(m/n),0,-1):
    if m%i == 0:
        if gcd(i,m//i) == 1:
            print(i)
            break
