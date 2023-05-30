def burger(n,x):
    if n==0:
        return 1
    elif x==1:
        return 0
    elif x<=1+burger(n-1,(2**(n+1)-3)//2):
        return burger(n-1,x-1)
    else:
        return 1+burger(n-1,x-1-(1+burger(n-1,(2**(n+1)-3)//2)))
n,x=map(int,input().split())
print(burger(n,x))
