def f(a,b):
    if a==b:
        return a
    else:
        return a^f(a+1,b)

if __name__ == '__main__':
    f()