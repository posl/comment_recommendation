Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(x,y):
    if x < y:
        x,y = y,x
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 4

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in range(1, m + 1):
    flag = True
    for j in range(n):
        if gcd(a[j], i) != 1:
            flag = False
            break
    if flag:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)

=======
Suggestion 5

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 6

def gcd(a,b):
    if a>b:
        a,b=b,a
    if a==0:
        return b
    return gcd(b%a,a)

n,m=map(int,input().split())
a=list(map(int,input().split()))
max_a=max(a)
cnt=[0]*(max_a+1)
for i in range(n):
    cnt[a[i]]+=1
ans=[]
for i in range(1,max_a+1):
    if cnt[i]==0:
        continue
    if gcd(i,max_a)==1:
        ans.append(i)
for i in range(1,m+1):
    if gcd(i,max_a)==1:
        ans.append(i)
ans=set(ans)
ans=list(ans)
ans.sort()
print(len(ans))
for i in ans:
    print(i)

=======
Suggestion 7

def gcd(x,y):
    while x:
        x,y = y%x,x
    return y

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = list(map(int, input().split()))
# 用于记录已经找到的满足条件的数
ans = [1] * (m + 1)
# 用于记录已经找到的满足条件的数的个数
cnt = 0
