def cal(n,x):
    if n==0:
        return 0
    if x==1:
        return 0
    if x<=1+2*cal(n-1,(2**(n+1)-1)//2):
        return cal(n-1,x-1)
    else:
        return 1+cal(n-1,x-(2**(n+1)-1)//2-1)
n,x=map(int,input().split())
print(cal(n,x))
