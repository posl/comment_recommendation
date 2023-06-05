def f(a,b):
    #print(a,b)
    if a==b:
        return a
    elif a+1==b:
        return a^b
    elif a+2==b:
        return a^b^(a+1)
    else:
        if a%2==0:
            if b%2==0:
                return f(a,b-1)^b
            else:
                return f(a,b-2)^b^(b-1)
        else:
            if b%2==0:
                return f(a+1,b)^a
            else:
                return f(a+2,b)^a^(a+1)

if __name__ == '__main__':
    f()