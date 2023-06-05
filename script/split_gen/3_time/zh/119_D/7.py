def find(s,t,x):
    if s[0]>x:
        return s[0]-x
    if t[-1]<x:
        return x-t[-1]
    l=0
    r=len(s)-1
    while l<r:
        mid=(l+r)//2
        if s[mid]==x:
            return 0
        elif s[mid]>x:
            r=mid
        else:
            l=mid+1
    if s[l]==x:
        return 0
    else:
        return min(s[l]-x,x-s[l-1])
a,b,q=map(int,input().split())
s=[]
t=[]
for i in range(a):
    s.append(int(input()))
for i in range(b):
    t.append(int(input()))
for i in range(q):
    x=int(input())
    print(min(find(s,t,x),find(t,s,x),find(s,t[x]),find(t,s[x])))
