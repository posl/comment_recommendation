def f(n,x):
    if n==0:
        return 0
    if x==1:
        return 0
    if x<=1+f(n-1,(2**(n+1)-3)//2):
        return f(n-1,x-1)
    if x==1+f(n-1,(2**(n+1)-3)//2)+1:
        return 1+f(n-1,(2**(n+1)-3)//2)
    if x<=1+f(n-1,(2**(n+1)-3)//2)+1+f(n-1,(2**(n+1)-3)//2):
        return 1+f(n-1,(2**(n+1)-3)//2)+f(n-1,x-1-f(n-1,(2**(n+1)-3)//2)-1)
    return 1+f(n-1,(2**(n+1)-3)//2)+f(n-1,(2**(n+1)-3)//2)
n,x=map(int,input().split())
print(f(n,x))
