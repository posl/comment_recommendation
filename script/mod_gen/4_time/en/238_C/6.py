def f(x):
    #f(x) is the number of positive integers at most x with the same number of digits as x.
    #f(x) = 10^(len(str(x))-1) + f(x-10^(len(str(x))-1)) if x>=10
    #f(x) = x if x<10
    if x<10:
        return x
    else:
        return 10**(len(str(x))-1) + f(x-10**(len(str(x))-1))

if __name__ == '__main__':
    f()