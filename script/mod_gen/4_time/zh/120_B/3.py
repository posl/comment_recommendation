def f(x,y):
    if x>y:
        x,y=y,x
    for i in range(1,x+1):
        if x%i==0 and y%i==0:
            a=i
    return a

if __name__ == '__main__':
    f()