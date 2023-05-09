def check(a,b,c,d):
    if a==c and b==d:
        return True
    if a==-c and b==-d:
        return True
    if a==d and b==-c:
        return True
    if a==-d and b==c:
        return True
    return False

if __name__ == '__main__':
    check()