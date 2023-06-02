Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(x,y):
    if x < y:
        x,y = y,x
    while y > 0:
        x,y = y,x % y
    return x

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 6

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

N,M = map(int,input().split())
A = list(map(int,input().split()))
A = list(set(A))
A.sort()
lcm = A[0]
for i in range(1,len(A)):
    lcm = lcm*A[i]//gcd(lcm,A[i])
count = 0
for i in range(1,M//lcm+1):
    if i%2==1:
        count += 1
        continue
    for j in range(len(A)):
        if i%A[j]==A[j]//2:
            count += 1
            break
print(count)

=======
Suggestion 7

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
