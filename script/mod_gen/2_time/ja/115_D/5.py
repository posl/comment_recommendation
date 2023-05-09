def f(n,x):
    if n==0:
        return 0 if x<=0 else 1
    elif x<=1+2*f(n-1,x-2):
        return f(n-1,x-2)
    else:
        return 1+2*f(n-1,x-2)-f(n-1,x-2-2*f(n-1,x-2))
n,x=map(int,input().split())
print(f(n,x))

if __name__ == '__main__':
    f()