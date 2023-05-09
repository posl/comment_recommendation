def f(a,b):
    if a%2==0:
        if b%2==0:
            return b-a+1
        else:
            return b-a+2
    else:
        if b%2==0:
            return b-a+2
        else:
            return b-a+1
