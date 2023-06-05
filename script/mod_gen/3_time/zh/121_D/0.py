def f(a,b):
    c=a
    for i in range(a+1,b+1):
        c=c^i
    return c

if __name__ == '__main__':
    f()