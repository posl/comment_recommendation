def isdamage(x,y,s,d):
    if x < s and y > d:
        return True
    else:
        return False

if __name__ == '__main__':
    isdamage()