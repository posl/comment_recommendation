def g(a,b):
    if b==0:
        return a
    else:
        return g(b,a%b)

if __name__ == '__main__':
    g()