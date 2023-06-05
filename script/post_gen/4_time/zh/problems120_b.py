Synthesizing 10/10 solutions

=======
Suggestion 1

def getGCD(x,y):
    if x < y:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x

=======
Suggestion 2

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b,k=map(int,input().split())
c=gcd(a,b)
cnt=0
for i in range(c,0,-1):
    if a%i==0 and b%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break

=======
Suggestion 3

def getKthCommonDivisor(A, B, K):
    if A > B:
        A, B = B, A
    count = 0
    for i in range(1, B + 1):
        if A % i == 0 and B % i == 0:
            count += 1
            if count == K:
                return i
    return 0

=======
Suggestion 4

def f(x,y):
    if x>y:
        x,y=y,x
    for i in range(1,x+1):
        if x%i==0 and y%i==0:
            a=i
    return a

=======
Suggestion 5

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

=======
Suggestion 6

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

=======
Suggestion 7

def f():
    A,B,K = map(int,input().split())
    L = []
    for i in range(1,101):
        if A % i == 0 and B % i == 0:
            L.append(i)
    print(L[-K])

f()

=======
Suggestion 8

def getDivisor(a, b):
    divisor = []
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            divisor.append(i)
    return divisor

=======
Suggestion 9

def solve():
    A, B, K = map(int, input().split())
    cnt = 0
    for i in range(1, 10000):
        if A % i == 0 and B % i == 0:
            cnt += 1
            if cnt == K:
                print(i)
                break

=======
Suggestion 10

def problem120_b():
    a,b,k = map(int, input().split())
    count = 0
    for i in range(1, max(a,b)+1):
        if a%i == 0 and b%i == 0:
            count += 1
            if count == k:
                print(i)
                break
