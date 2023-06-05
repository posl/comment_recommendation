def isConnect(a,b):
    #print(a,b)
    if a==b:
        return True
    if a==1 and b==2:
        return True
    if a==1 and b==3:
        return True
    if a==1 and b==4:
        return True
    if a==1 and b==5:
        return True
    if a==2 and b==3:
        return True
    if a==2 and b==4:
        return True
    if a==2 and b==5:
        return True
    if a==3 and b==4:
        return True
    if a==3 and b==5:
        return True
    if a==4 and b==5:
        return True
    return False

if __name__ == '__main__':
    isConnect()