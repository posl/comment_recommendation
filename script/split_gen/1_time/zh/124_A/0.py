def coins(a,b):
    if a>b:
        return a+a-1
    elif a<b:
        return b+b-1
    else:
        return a+b
