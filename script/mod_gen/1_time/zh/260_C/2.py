def f(n,x,y):
    if n==1:
        return 0
    else:
        return 1+f(n-1,x,y)+f(n-1,x,y)

if __name__ == '__main__':
    f()