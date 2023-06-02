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

def gcd(x,y):
    if x < y:
        x,y = y,x
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
a.sort()
b=[]
for i in range(1,m+1):
    flag=0
    for j in a:
        if gcd(i,j)==1:
            flag=1
            break
    if flag==0:
        b.append(i)
print(len(b))
for i in b:
    print(i)

=======
Suggestion 4

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 5

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
b=[0]*(m+1)
for i in a:
    for j in range(i,m+1,i):
        b[j]+=1
ans=0
for i in range(1,m+1):
    if b[i]==1:
        ans+=1
print(ans)
for i in range(1,m+1):
    if b[i]==1:
        print(i)

=======
Suggestion 6

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

=======
Suggestion 7

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 8

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
maxA=A[-1]
listA=[True]*(maxA+1)
for i in range(N):
    for j in range(A[i],maxA+1,A[i]):
        listA[j]=False
ans=[]
for i in range(1,M+1):
    if listA[i]:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)
