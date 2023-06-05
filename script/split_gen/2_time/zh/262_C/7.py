def find(a,b,c):
    if a>b:
        a,b=b,a
    if b>c:
        b,c=c,b
    if a>b:
        a,b=b,a
    return a,b,c
