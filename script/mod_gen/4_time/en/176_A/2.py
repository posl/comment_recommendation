def takoyaki(n,x,t):
    if(n%x==0):
        return (n//x)*t
    else:
        return (n//x+1)*t
n,x,t = map(int,input().split())
print(takoyaki(n,x,t))
