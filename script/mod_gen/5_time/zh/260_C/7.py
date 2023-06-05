def f(n,x,y):
    if n == 1:
        return 0
    if n == 2:
        return x
    if n == 3:
        return x + y
    return f(n-1,x,y) + f(n-2,x,y) + f(n-3,x,y)

if __name__ == '__main__':
    f()