def f(x):
    return x - 10**(len(str(x))-1) + 1

if __name__ == '__main__':
    f()