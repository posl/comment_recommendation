def calc(s):
    l=len(s)
    if l<3:
        return l
    elif l%3==0:
        return l//3*2
    else:
        return l//3*2+1
