def cal(n,x):
    if n==0:
        return 0
    elif x==1:
        return 0
    elif x<=2**(n+1)-3:
        return cal(n-1,x-1)
    elif x==2**(n+1)-2:
        return 2**n-1
    elif x==2**(n+1)-1:
        return 2**n
    elif x<=2**(n+2)-3:
        return 2**n-1+cal(n-1,x-2**(n+1)+1)
    else:
        return 2**(n+1)-1
n,x=map(int,input().split())
print(cal(n,x))
