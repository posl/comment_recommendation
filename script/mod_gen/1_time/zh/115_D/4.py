def f(n,x):
    if n==0:
        return 0
    elif x==1:
        return 0
    elif x<=1+f(n-1,x-1):
        return f(n-1,x-1)
    elif x==2+f(n-1,x-1):
        return 1+g(n-1)
    elif x<=2+2*f(n-1,x-2):
        return 1+g(n-1)+f(n-1,x-2)
    else:
        return 1+2*g(n-1)

if __name__ == '__main__':
    f()