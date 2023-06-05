def check(a,b,c):
    if a < b < c:
        if (a,b) in edge and (b,c) in edge and (c,a) in edge:
            return True
    return False
