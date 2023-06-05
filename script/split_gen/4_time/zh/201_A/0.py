def isAP(a,b,c):
    if a-b == b-c:
        return True
    else:
        return False
a,b,c = map(int,input().split())
