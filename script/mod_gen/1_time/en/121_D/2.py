def f(a,b):
    if a%2==0:
        if b%2==0:
            return a^b
        else:
            return a^b^1
    else:
        if b%2==0:
            return a^b^1
        else:
            return a^b

if __name__ == '__main__':
    f()