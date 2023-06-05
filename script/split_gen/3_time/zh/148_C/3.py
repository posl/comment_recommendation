def cal(x,y):
    if x>y:
        return cal(y,x)
    else:
        if y%x==0:
            return x
        else:
            return cal(y%x,x)
