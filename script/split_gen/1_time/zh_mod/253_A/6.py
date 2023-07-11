def find_mid(a,b,c):
    if a<b<c or c<b<a:
        return b
    elif b<a<c or c<a<b:
        return a
