def f(n):
    if n==1:
        return True
    elif n%2==0:
        return f(n/2)
    else:
        return F

if __name__ == '__main__':
    f()