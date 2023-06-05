def make_takoyaki(n,x,t):
    if n%x == 0:
        return n//x * t
    else:
        return (n//x + 1) * t

if __name__ == '__main__':
    make_takoyaki()