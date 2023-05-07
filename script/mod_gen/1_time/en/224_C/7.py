def check(a,b,c):
    if a[0]==b[0] and b[0]==c[0]:
        return False
    if a[1]==b[1] and b[1]==c[1]:
        return False
    if (a[0]-b[0])*(b[1]-c[1])==(a[1]-b[1])*(b[0]-c[0]):
        return False
    return True

if __name__ == '__main__':
    check()