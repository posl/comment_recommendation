def pow(a,b,c):
    if a<0 and b>0:
        if c%2==0:
            return '>'
        else:
            return '<'
    elif a<0 and b<0:
        if c%2==0:
            return '='
        else:
            return '<'
    elif a>0 and b<0:
        if c%2==0:
            return '='
        else:
            return '>'
    elif a==0 and b==0:
        return '='
    elif a==0:
        return '<'
    elif b==0:
        return '>'
    elif a>0 and b>0:
        return '>'
a,b,c = map(int,input().split())
print(pow(a,b,c))
