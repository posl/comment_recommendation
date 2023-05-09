def check(a,s):
    if a==0:
        if s==0:
            return True
        else:
            return False
    else:
        if s%a==0:
            return True
        else:
            return False
