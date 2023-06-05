def check(x,y,z):
    if x==y and x!=z:
        return True
    elif x==z and x!=y:
        return True
    elif y==z and y!=x:
        return True
    else:
        return False
x,y,z=map(int,input().split())
